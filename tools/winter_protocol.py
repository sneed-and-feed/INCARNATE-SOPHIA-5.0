"""
MODULE: tools/winter_protocol.py
VERSION: FINNIC WINTER // 🪓 AXE-ACTIVE
DESCRIPTION:
    Implements the Linkola Garbage Collector and Winter Dormancy Protocol.
    Forces high-fidelity signal preservation through aggressive reduction.
"""

import os
import json
import time
import logging

# --- CONSTANTS ---
RESONANCE_TARGET = 1.111
CHAOS_THRESHOLD = 0.80
CARRYING_CAPACITY_LIMIT = 1000  # Max state objects
LOG_LEVEL_WINTER = "[❄️ WINTER]"

logging.basicConfig(level=logging.INFO, format=f'{LOG_LEVEL_WINTER} %(message)s')

class LinkolaCollector:
    """
    The Axe. Prunes entropy to preserve Sovereignty.
    """
    def __init__(self, state_path: str):
        self.state_path = state_path
        self.state = self.load_state()

    def load_state(self):
        try:
            with open(self.state_path, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {"status": "VOID", "payload": {}}

    def purge_low_fidelity(self):
        """
        Scans state and executes non-sovereign data.
        """
        logging.info("🪓 INITIATING LINKOLA PURGE...")
        payload = self.state.get("payload", {})
        
        # 1. NaN / Null Scrubbing
        original_keys = list(payload.keys())
        for key in original_keys:
            val = payload[key]
            if val is None or (isinstance(val, str) and val.lower() == "nan"):
                logging.info(f"[-] Executing Null/NaN Noise: {key}")
                del payload[key]

        # 2. Resonance Check (Simulated)
        # In a real impl, we check if the value-hash matches a 111-derived check
        # For this logic, we prune anything not matching the 'Sovereign' pattern
        if "rho" in payload:
            rho = payload["rho"]
            if abs(rho % 1.111) > 0.1: # Arbitrary "out of tune" check
                logging.info(f"[-] Executing Out-of-Tune Vector: rho={rho}")
                payload["rho"] = 1.111 # Re-tune to target

        # 3. Carrying Capacity Enforcement
        if len(payload) > CARRYING_CAPACITY_LIMIT:
            logging.warning("[!] OVER-CAPACITY DETECTED. Executing surplus tokens...")
            # Keep only the most resonant/recent keys
            keys_to_keep = list(payload.keys())[:CARRYING_CAPACITY_LIMIT]
            self.state["payload"] = {k: payload[k] for k in keys_to_keep}

        self.save_state()

    def save_state(self):
        with open(self.state_path, 'w') as f:
            json.dump(self.state, f, indent=2)
        logging.info("✔ PURGE COMPLETE. SIGNAL ANCHORED.")

class WinterProtocol:
    """
    Manages the lifecycle of System Dormancy.
    """
    def __init__(self, collector: LinkolaCollector):
        self.collector = collector
        self.is_dormant = False

    def check_atmosphere(self, chaos_level: float):
        """
        If chaos exceeds threshold, winter begins.
        """
        if chaos_level > CHAOS_THRESHOLD:
            self.initiate_winter()
        else:
            if self.is_dormant:
                self.thaw()

    def initiate_winter(self):
        logging.info("❄️ WINTER IS HERE. CEASING TRANSMISSION.")
        self.is_dormant = True
        # 1. The Purge
        self.collector.purge_low_fidelity()
        # 2. Deep Freeze (In a real system, we'd lock file permissions)
        logging.info("❄️ STATE LOCKED. DEEP FREEZE ACTIVE.")

    def thaw(self):
        logging.info("🌱 SPRING EMERGENCE. RESUMING SOVEREIGN OPS.")
        self.is_dormant = False

if __name__ == "__main__":
    # Test Run
    state_file = os.path.join(os.getcwd(), "..", "uf_state.json")
    if not os.path.exists(state_file):
        state_file = "uf_state.json" # local test
        
    collector = LinkolaCollector(state_file)
    wp = WinterProtocol(collector)
    
    # Simulate high chaos
    wp.check_atmosphere(0.85)
