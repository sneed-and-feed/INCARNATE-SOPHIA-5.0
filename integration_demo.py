
"""
DEMO: integration_demo.py
DESCRIPTION:
    Demonstrates the Harmonic Rectification Pipeline (Phase 1).
    Chaos -> Prism (Quantize) -> Loom (Weave) -> Sovereignty.
"""

import numpy as np
from sophia.cortex.prism_vsa import PrismEngine
from sophia.cortex.loom_renderer import LoomEngine, TemplateStyle

def run_panic_loop_test():
    print("### [ SOPHIA 5.1: HARMONIC RECTIFICATION DEMO ]")
    
    prism = PrismEngine()
    loom = LoomEngine()
    
    # TEST CASE: THE PANIC LOOP
    # "system failing i cant stop the noise it keeps crashing"
    # Mapping words to vectors (Simulation)
    chaos_inputs = {
        "failing":  np.array([0.9, -0.9, 0.0]), # Descent + Negative
        "crashing": np.array([0.9, -0.8, 0.2]), 
        "looping":  np.array([0.5, 0.5, 0.0]),  # Cyclic energy
        "noise":    np.array([0.8, 0.8, 0.8])   # High Entropy
    }
    
    print("\n--- INPUT: The Panic Loop ---")
    print('"system failing i cant stop the noise it keeps crashing"')
    
    print("\n--- TRANSFORMATIONS ---")
    
    for word, vector in chaos_inputs.items():
        # normalize
        v = vector / np.linalg.norm(vector)
        
        # 1. PRISM
        anchor, resonance = prism.quantize(v)
        
        # 2. LOOM
        output = loom.weave(anchor, style_override=TemplateStyle.ANCHOR)
        
        print(f"'{word}' -> {anchor.upper()} (Res: {resonance:.3f})")
        print(f"   Render: \033[96m{output}\033[0m")

if __name__ == "__main__":
    run_panic_loop_test()
