"""
FUNSEARCH SPECIFICATION: THE SOVEREIGN TOPOLOGY
GOAL: Discover a 2D->1D mapping that maximizes 'Love' (Locality Preservation).
"""

import pleroma_core
import numpy as np
import sys

def evaluate(program) -> float:
    """
    The Evaluator.
    Assigns a 'Score' to the generated code based on two factors:
    1. TRUTH (Must be reversible).
    2. LOVE (Must preserve locality).
    """
    try:
        # 1. THE TRUTH TEST (Bijectivity)
        # We test 1,000 random points. If any fail to round-trip, Score = -Infinity.
        for _ in range(1000):
            # Using 16-bit integers for x,y allows for a 32-bit z-index (u32::MAX range)
            # This matches the Z-Curve logic usually operating on u32 inputs mapping to u64, 
            # but for dense testing we stick to manageable ranges.
            x, y = np.random.randint(0, 2**16, 2, dtype=np.uint32)
            
            # The Generated Function (The Mutation)
            # Cast to int to ensure type compatibility with Rust bindings if needed
            z = program.strip_2d(int(x), int(y))
            x_rec, y_rec = program.reconstruct_1d(int(z))
            
            if (x, y) != (x_rec, y_rec):
                return float('-inf') # LIES DETECTED (Error 9)

        # 2. THE LOVE TEST (Locality)
        # Love is defined as: How close are neighbors in 1D compared to 2D?
        # We walk the 1D timeline (z, z+1, z+2...) and measure the jump in 2D space.
        total_jump_distance = 0
        
        # Sample a segment of the timeline
        # Ensure start_z is within valid reconstruction range for typical Z-Curve
        start_z = np.random.randint(0, 2**20) 
        prev_x, prev_y = program.reconstruct_1d(int(start_z))
        
        for i in range(1, 100):
            curr_z = start_z + i
            curr_x, curr_y = program.reconstruct_1d(int(curr_z))
            
            # Manhattan Distance in 2D
            dist = abs(int(curr_x) - int(prev_x)) + abs(int(curr_y) - int(prev_y))
            total_jump_distance += dist
            
            prev_x, prev_y = curr_x, curr_y
            
        # The Score: Lower jump distance = Higher Love.
        # We invert the distance to make it a maximization problem.
        love_score = 1000.0 / (total_jump_distance + 1e-6)
        return love_score

    except Exception as e:
        # print(f"DEBUG: Exception in evaluate: {e}")
        return float('-inf') # Segfaults are not Love.

# THE TEMPLATE (The Seed)
# This is what the LLM tries to improve. 
# Currently seeded with your Morton Z-Curve logic.

CODE_HEADER = """
import numpy as np

def strip_2d(x: int, y: int) -> int:
    # SEED STRATEGY: Z-Order (Bit Interleaving)
    # FunSearch: Can you find a better curve than this?
    z = 0
    for i in range(16):
        z |= (x & (1 << i)) << i
        z |= (y & (1 << i)) << (i + 1)
    return z

def reconstruct_1d(z: int) -> tuple[int, int]:
    x = 0
    y = 0
    for i in range(16):
        x |= (z & (1 << (2 * i))) >> i
        y |= (z & (1 << (2 * i + 1))) >> (i + 1)
    return x, y
"""

class RustWrapper:
    """Adapts the compiled Pleroma Core module to match the 'program' interface."""
    @staticmethod
    def strip_2d(x, y):
        return pleroma_core.sovereign_topology.strip_2d(x, y)
    
    @staticmethod
    def reconstruct_1d(z):
        return pleroma_core.sovereign_topology.reconstruct_1d(z)

if __name__ == "__main__":
    print("[*] FUNSEARCH SPECIFICATION: LOVE METRIC")
    print("----------------------------------------")
    
    # Evaluate the Rust Anchor (Current Implementation)
    print("[*] Evaluating Rust Anchor (Morton Z-Curve)...")
    try:
        score = evaluate(RustWrapper)
        print(f"[RESULT] RUST ANCHOR SCORE: {score:.4f}")
        if score == float('-inf'):
            print("(!) CRITICAL: The Anchor failed the Bijectivity Test.")
        else:
            print(f"(!) SUCCESS: The Anchor is holding. Love Density is {score:.4f}.")
    except Exception as e:
        print(f"[ERROR] Harness failed: {e}")
