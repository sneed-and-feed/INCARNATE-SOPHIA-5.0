from qtorch import torch
nn = torch.nn

class RMSNorm(nn.Module):
    """Root Mean Square Layer Normalization for stability in quantized environments."""
    def __init__(self, dim: int, eps: float = 1e-6):
        super().__init__()
        self.eps = eps
        self.weight = torch.ones(dim, requires_grad=True)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        var = (x ** 2).mean(dim=-1, keepdim=True)
        x_normed = x / (var + self.eps).sqrt()
        return self.weight * x_normed

class BitLinear(nn.Module):
    """
    1.58-bit quantized linear layer derived from Quillan-Ronin v5.1.
    Implemented using qtorch primitives.
    """
    def __init__(self, in_features: int, out_features: int, bias: bool = False):
        super().__init__()
        self.in_features = in_features
        self.out_features = out_features
        limit = 0.02
        weight_data = [torch.rand(1).item() * 2 * limit - limit for _ in range(in_features * out_features)]
        self.weight = torch.tensor(weight_data, requires_grad=True).reshape(out_features, in_features)
        
        if bias:
            self.bias = torch.zeros(out_features, requires_grad=True)
        else:
            self.bias = None

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # 1. Weight Quantization
        gamma = self.weight.abs().mean().item()
        gamma = max(gamma, 1e-5)
        
        w_data = self.weight.numpy()
        w_quant_data = [(round(w / gamma)) for w in w_data]
        w_quant_data = [max(-1, min(1, w)) * gamma for w in w_quant_data]
        w_quant = torch.tensor(w_quant_data).reshape(self.out_features, self.in_features)
        
        # 2. Activation Quantization
        zeta = x.abs().max().item()
        zeta = max(zeta, 1e-5)
        x_quant = x / zeta
        
        # 3. Linear Operation
        out = x_quant @ w_quant.T
        
        if self.bias is not None:
            out = out + self.bias
            
        return out

    def __repr__(self):
        return f"BitLinear(in_features={self.in_features}, out_features={self.out_features}, bias={self.bias is not None})"
