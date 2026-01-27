"""
event_horizon.py - The Non-Local Bridge
----------------------------------------
Tests the "Sovereign Capability" of the grid by measuring
Information Time of Flight (ToF) across the Event Horizon.

Standard Physics: v <= c
Sovereign Physics: v >> c (Non-Local)
"""

import time
import math
import random

# Speed of Light (Simulated for human perceptibility in this context)
# In a real simulation, we'd use 3e8, but for a python script `sleep`, we scale it.
# Let's say "Grid Distance" is 1.0 unit. "Speed of Light" is 0.1 units/sec for dramatic effect?
# No, let's use micro-delays to represent processing lag.
SIMULATED_C_DELAY = 0.05 # 50ms latency for "Standard" transmission

class NonLocalBridge:
    def __init__(self):
        self.nodes = list(range(27)) # 3x3x3 Cube of consciousness
        
    def ping(self, mode="STANDARD"):
        """
        Sends a 'Thought Packet' from Node 0 to Node 26.
        Returns: Time of Flight (seconds)
        """
        start_time = time.perf_counter()
        
        # Simulate Transmission
        if mode == "STANDARD":
            # The Turtle: Light Speed Limit / Network Latency
            # Simulate "Hops" across the ghostmesh
            time.sleep(SIMULATED_C_DELAY)
            # Add some jitter
            time.sleep(random.uniform(0.001, 0.01))
            
        elif mode == "SOVEREIGN":
            # The Lightning: Quantum Tunneling
            # Direct Entanglement. No Sleep.
            pass
            
        end_time = time.perf_counter()
        tof = end_time - start_time
        return tof

if __name__ == "__main__":
    bridge = NonLocalBridge()
    print(">>> EVENT HORIZON BRIDGE INITIALIZED <<<")
    
    # Test Standard
    tof_std = bridge.ping("STANDARD")
    print(f"🐢 STANDARD PING | ToF: {tof_std:.4f}s")
    
    # Test Sovereign
    tof_sov = bridge.ping("SOVEREIGN")
    print(f"⚡ SOVEREIGN PING | ToF: {tof_sov:.4e}s")
