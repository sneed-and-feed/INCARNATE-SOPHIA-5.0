
import sys
import os

# Ensure we can import modules from the parent directory
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ghostmesh import SovereignGrid
import uhif

def test_luoshu_invariant():
    """Verifies that the 27-Node Grid still sums to 15."""
    grid = SovereignGrid()
    assert grid.invariant == 15.0, "CRITICAL FAILURE: THE ARCHONS HAVE BREACHED THE SQUARE."

def test_reality_density():
    """Ensures we aren't drifting into the void."""
    from hyper_sovereign import HyperManifold
    # Ensure we have a default state that passes
    hm = HyperManifold()
    assert hm.reality_density >= 1.0, "WARNING: REALITY IS TOO THIN. INCREASE FUZZ."

def test_gateway_safety():
    """Ensures the gateways remain guarded (Benevolent Export)."""
    from gateways import TensorGate
    # Test that calling export doesn't crash even if Torch/Numpy is missing
    grid_mock = [1.0] * 27
    
    # These should print messages but NOT raise exceptions
    try:
        TensorGate.export_to_torch(grid_mock)
        TensorGate.export_to_numpy(grid_mock)
    except Exception as e:
        assert False, f"CRITICAL: GATEWAYS ARE UNSTABLE. {e}"
