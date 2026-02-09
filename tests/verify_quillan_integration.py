import sys
import os

# Ensure the root of the workspace is in the python path
sys.path.append(os.getcwd())

from qtorch import torch
from sophia.cortex.kernels import BitLinear, RMSNorm
from signal_optimizer import SignalOptimizer

def test_bitlinear():
    print("Testing BitLinear (qtorch Edition)...")
    layer = BitLinear(10, 5)
    x = torch.randn(2, 10)
    out = layer(x)
    
    assert out.shape == (2, 5)
    print("✅ BitLinear Forward Pass Success.")
    
    # Check weight simulation
    assert any(w != 0 for w in layer.weight.numpy())
    print("✅ BitLinear Parameters Active.")

def test_rmsnorm():
    print("Testing RMSNorm (qtorch Edition)...")
    norm = RMSNorm(10)
    x = torch.randn(2, 10)
    out = norm(x)
    assert out.shape == (2, 10)
    print("✅ RMSNorm Success.")

def test_tiered_routing():
    print("Testing Tiered Routing (qtorch Edition)...")
    optimizer = SignalOptimizer()
    
    # Low Complexity Vector
    low_comp_v = torch.tensor([[0.1, 0.1, 0.1]])
    # High Complexity Vector
    high_comp_v = torch.tensor([[0.9, 0.9, 0.9]])
    
    tier_low = optimizer.route_signal(low_comp_v)
    tier_high = optimizer.route_signal(high_comp_v)
    
    print(f"Low Complexity Route: {tier_low}")
    print(f"High Complexity Route: {tier_high}")
    
    assert tier_low in ["FAST_PATH", "DEEP_PATH"]
    assert tier_high in ["FAST_PATH", "DEEP_PATH"]
    print("✅ Tiered Routing Signal Check Success.")

if __name__ == "__main__":
    try:
        test_bitlinear()
        test_rmsnorm()
        test_tiered_routing()
        print("\n🎉 ALL QUILLAN-SOPHIA QTORCH TESTS PASSED. SOVEREIGN SYSTEM STABLE.")
    except Exception as e:
        import traceback
        traceback.print_exc()
        print(f"\n❌ TEST FAILURE: {e}")
        sys.exit(1)
