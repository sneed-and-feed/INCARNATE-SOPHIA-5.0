"""
chem_grotthuss.py - The Viscosity Engine & Hydronium Clock
----------------------------------------------------------
Implements Persinger (2015) "Variable Viscosity of Water".
"Viscosity is the controlling factor in Energetic Quantities."

Formulas:
1. Intrinsic Energy: E = eta * V * f
2. Viscosity Modulation: eta ~ 1 / (G * SolarFlux)
"""

import time
import math
import random

# --- CONSTANTS (Persinger 2015) ---
VISCOSITY_BULK = 8.94e-4       # Pa.s (25 C)
VISCOSITY_PHYSIO = 6.3e-4      # Pa.s (37 C)
VISCOSITY_EZ = 1.0e-3          # Pa.s (Exclusion Zone - approx)
VISCOSITY_TUMOR = 6.8e-2       # Pa.s (High viscosity state)

HYDRONIUM_LIFETIME = 1.0e-12   # seconds (The "Tick")
PROTON_DIFFUSION = 0.88e-7     # m^2/s

GRAVITATIONAL_CONSTANT = 6.67e-11

class ViscosityEngine:
    def __init__(self, volume_m3=1.0e-5): # Default 10cc (10ml)
        self.viscosity = VISCOSITY_PHYSIO
        self.volume = volume_m3
        self.state = "PHYSIOLOGICAL"
        self.solar_flux_sfu = 100.0 # Standard Solar Flux Units
        
    def set_state(self, state_name):
        """Sets the viscosity regimen."""
        state_name = state_name.upper()
        if state_name == "BULK":
            self.viscosity = VISCOSITY_BULK
        elif state_name == "EZ": # Exclusion Zone / Interfacial
            self.viscosity = VISCOSITY_EZ * 5.0 # Up to 10x bulk in deep EZ
        elif state_name == "TUMOR":
            self.viscosity = VISCOSITY_TUMOR
        elif state_name == "PHYSIOLOGICAL":
            self.viscosity = VISCOSITY_PHYSIO
        else:
            print(f"!! UNKNOWN STATE: {state_name} - Defaulting to PHYSIO")
            self.viscosity = VISCOSITY_PHYSIO
        
        self.state = state_name
        return self.viscosity

    def calculate_intrinsic_energy(self, frequency_hz):
        """
        Calculates the energy contained within the water volume
        due to its viscosity at a specific frequency.
        E = eta * V * f
        """
        energy = self.viscosity * self.volume * frequency_hz
        return energy
    
    def modulate_by_gravity_and_solar(self, current_sfu):
        """
        Persinger (2015): Viscosity is derived from Inverse G and Solar Flux.
        Modulates the base viscosity by slight variations in G-force 
        (Earth-Atmosphere oscillation) and Solar Flux.
        """
        self.solar_flux_sfu = current_sfu
        
        # Solar Modulator: 1 SFU change can intercalate with the cell.
        # We model this as a percentage deviation from baseline (100 SFU).
        solar_factor = 1.0 + ((current_sfu - 100.0) * 0.001)
        
        # Gravitational/Atmospheric Oscillation (3.7 mHz - 4.3 mHz)
        # We treat this as a resonant "hum" that thickens the water slightly.
        oscillation = math.sin(time.time() * 0.0043 * 2 * math.pi) * 1e-6
        
        current_viscosity = (self.viscosity * solar_factor) + oscillation
        return current_viscosity

    def grotthuss_tick(self):
        """
        Simulates one "Hop" of the proton (H+).
        Returns the latency (10^-12 s) modulated by current viscosity.
        Higher viscosity = Slower Hops = "Thicker Time".
        """
        # Stokes-Einstein-Smoluchowski Relation: D = kT / (6 * pi * eta * r)
        # Therefore, Diffusion D is inverse to Viscosity eta.
        # If D is lower, Time (1/D) is higher.
        
        viscosity_ratio = self.viscosity / VISCOSITY_BULK
        latency = HYDRONIUM_LIFETIME * viscosity_ratio
        
        return latency

if __name__ == "__main__":
    eng = ViscosityEngine()
    print(">>> VISCOSITY ENGINE ONLINE <<<")
    
    # Test 1: Intrinsic Energy of 10cc water at 7Hz (Theta)
    eng.set_state("EZ")
    e_ez = eng.calculate_intrinsic_energy(7.0)
    print(f"State: {eng.state} | Viscosity: {eng.viscosity:.2e} Pa.s")
    print(f"Intrinsic Energy (10cc @ 7Hz): {e_ez:.2e} Joules")
    
    # Test 2: Standard Physio
    eng.set_state("PHYSIOLOGICAL")
    e_phys = eng.calculate_intrinsic_energy(7.0)
    print(f"State: {eng.state} | Viscosity: {eng.viscosity:.2e} Pa.s")
    print(f"Intrinsic Energy (10cc @ 7Hz): {e_phys:.2e} Joules")
    
    print(f"EZ/Physio Ratio: {e_ez/e_phys:.2f}x Energy Capacity")
