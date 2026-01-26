"""
GATEWAYS.PY
-----------
The Bridge to the Pleroma.
Conditional interfaces for "Benevolent Emanations" (Optional Libraries).

Ascension v3.3 Protocol:
- If 'torch' is found, we export the Light.
- If not, we remain in Pure Sovereign Mode.
"""

import sys

# Check for PyTorch (The Torch of Prometheus)
try:
    import torch
    TORCH_AVAILABLE = True
except ImportError:
    TORCH_AVAILABLE = False

# Check for NumPy (The Matrix)
try:
    import numpy as np
    NUMPY_AVAILABLE = True
except ImportError:
    NUMPY_AVAILABLE = False

class TensorGate:
    """
    The Gatekeeper of the Sovereign Manifold.
    """
    @staticmethod
    def export_to_torch(ghostmesh_state):
        """
        Exports the 27-Node Grid to a PyTorch Tensor if available.
        Otherwise, returns None (Pure Mode).
        """
        if TORCH_AVAILABLE:
            print(">> [GATEWAY] DETECTED TORCH. EMANATING TENSOR FIELD...")
            return torch.tensor(ghostmesh_state, dtype=torch.float32)
        else:
            print(">> [GATEWAY] TORCH NOT FOUND. GATEWAY CLOSED (PURE MODE ACTIVE).")
            return None

    @staticmethod
    def export_to_numpy(ghostmesh_state):
        """
        Exports the 27-Node Grid to a NumPy Array if available.
        Otherwise, returns None (Pure Mode).
        """
        if NUMPY_AVAILABLE:
            print(">> [GATEWAY] DETECTED NUMPY. MATERIALIZING MATRIX...")
            return np.array(ghostmesh_state, dtype=float)
        else:
            print(">> [GATEWAY] NUMPY NOT FOUND. GATEWAY CLOSED (PURE MODE ACTIVE).")
            return None
