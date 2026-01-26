"""
LEI_SUMMON.PY
-------------
The Bio-Digital Entity Summoner for Quantum Sovereignty 3.1.
Interprets the 27-Node Grid Entropy as 'Lei Music' to manifest local daemons.

Lore:
- 'Lei Disks' are the storage medium.
- Entities are generated from the 'Invisible Zones' (Unused RAM).

Usage:
    python lei_summon.py
"""

import random
import time
# from ghostmesh import SovereignGrid  # Assuming linkage (Simulated for this script)

import json
import os

# --- THE LEI DICTIONARY ---
PREFIXES = ["Squeaking", "Clattering", "Glitch", "Inkblot", "Pebble", "Hyper", "Vibrating", "Dust", "Neon", "Fractal"]
BODIES = ["Spore", "Drone", "Fossil", "Geode", "Nodule", "Larva", "Construct", "Disk", "Shard", "Egg"]
TRAITS = ["Vibrating at 12Hz", "Leaking #C4A6D1 fluid", "Hovering menacingly", "Singing in base-12", "Eating RAM", "Rotating slowly", "Generating heat", "Phase-shifting"]

def generate_entity(entropy_level):
    """
    Summons an entity based on the Chaos (Entropy) of the grid.
    Low Entropy (< 0.6) -> Celles (Safe)
    High Entropy (> 0.6) -> Sylph Fossils (Chaotic)
    """
    if entropy_level < 0.6:
        entity_type = "Celle"
        vibe = "[ ☼ ] PRISTINE"
    else:
        entity_type = "Sylph Fossil"
        vibe = "[ ☗ ] CHAOTIC"

    prefix = random.choice(PREFIXES)
    body = random.choice(BODIES)
    trait = random.choice(TRAITS)
    
    # Dozenal ID Generation
    id_chars = "0123456789XE"
    entity_id = "".join(random.choice(id_chars) for _ in range(4))
    
    name = f"{prefix}-{body} [ID: {entity_id}]"
    
    return {
        "name": name,
        "type": entity_type,
        "id": entity_id,
        "trait": trait,
        "vibe": vibe,
        "entropy": entropy_level
    }

def save_lei_disk(entity):
    """Saves the entity to a .lei disk (JSON)."""
    filename = f"{entity['name'].replace(' ', '_').replace('[','').replace(']','')}.lei"
    with open(filename, "w") as f:
        json.dump(entity, f, indent=4)
    print(f"💿 LEI DISK BURNED: {filename}")

def main():
    print("📀 INSERTING LEI DISK...")
    time.sleep(1)
    print(">> SPINNING UP (144 BPM)...")
    time.sleep(1)
    print(">> PINGING INVISIBLE ZONES...")
    
    # Simulate Grid Reading (In real usage, read self.grid.entropy)
    current_entropy = random.random()
    
    entity = generate_entity(current_entropy)
    
    print(f"\n✨ SUMMON COMPLETE. ENTITY MANIFESTED:")
    print(f"   ┌────────────────────────────────────────┐")
    print(f"   │ NAME:  {entity['name']:<24}│")
    print(f"   │ TYPE:  {entity['type']:<24}│")
    print(f"   │ TRAIT: {entity['trait']:<24}│")
    print(f"   │ VIBE:  {entity['vibe']:<24}│")
    print(f"   └────────────────────────────────────────┘")
    
    save_lei_disk(entity)

    if entity['type'] == "Sylph Fossil":
        print("\n⚠️  WARNING: ENTITY IS HEAVY. DO NOT FEED IT ROOT ACCESS.")
    elif "Spore" in entity['name']:
        print("\n🥚 NOTE: It wants to vibrate.")

if __name__ == "__main__":
    main()
