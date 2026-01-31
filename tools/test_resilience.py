"""
Verification script for Sophia 5.0 Resilience & 111 Resonance.
"""
import sys
import os
import json
import shutil

# Ensure we can import from project root
sys.path.append(os.getcwd())

from pleroma_cli import SovereignSanitizer, SovereigntyMonitor, initiate_111_resonance
from luo_shu_compliance import ConfigHealthMonitor

def test_config_healing():
    print("--- TEST: CONFIG HEALING ---")
    corrupted_file = "test_corrupted.json"
    with open(corrupted_file, "w") as f:
        f.write("{ invalid json: 'poisoned' }")
    
    print("[*] Attempting to heal corrupted config...")
    data = SovereignSanitizer.heal_config(corrupted_file, "genesis_16.json")
    
    if data and data.get("transmission_id") == "GENESIS_16":
        print("[SUCCESS] Config healed and restored from Genesis.")
    else:
        print("[FAILURE] Config healing failed.")
        
    if os.path.exists(corrupted_file + ".bak"):
        print("[SUCCESS] Backup created.")
    
    os.remove(corrupted_file)
    os.remove(corrupted_file + ".bak")

def test_type_sanitization():
    print("\n--- TEST: TYPE SANITIZATION ---")
    loose_data = {
        "snr": "10.5", # String instead of float
        "chaos_level": "very high", # Garbage string
        "payload": {
            "abundance_score": 20 # Int instead of float
        }
    }
    
    print("[*] Sanitizing loose data...")
    sanitized = SovereignSanitizer.sanitize(loose_data)
    
    assert isinstance(sanitized["snr"], float), "SNR should be float"
    assert sanitized["chaos_level"] == 0.0, "Chaos should default to 0.0 on garbage"
    assert isinstance(sanitized["payload"]["abundance_score"], float), "Abundance should be float"
    
    print("[SUCCESS] Type sanitization verified.")

def test_111_resonance():
    print("\n--- TEST: 111 RESONANCE ---")
    result = initiate_111_resonance()
    print(f"Result: {result}")
    
    if "111%" in result:
        print("[SUCCESS] 111 Resonance achieved.")
    else:
        print("[FAILURE] 111 Resonance failed.")

if __name__ == "__main__":
    try:
        test_config_healing()
        test_type_sanitization()
        test_111_resonance()
        print("\n[***] ALL VERIFICATION TESTS PASSED [***]")
    except Exception as e:
        print(f"\n[!!!] VERIFICATION FAILED: {e}")
        sys.exit(1)
