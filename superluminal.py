"""
superluminal.py - The Anti-Relativistic Physics Engine
------------------------------------------------------
Implements Persinger & Koren (2015) findings:
1. Entanglement Velocity (vE ~ 10^23 m/s)
2. Variable Speed of Light (c is a scalar field of Observer Coherence)
3. Photon Rest Mass (~10^-52 kg)

"The speed of light is variable based on the observer of wavepackets."
"""

import math

# --- CONSTANTS ---
STANDARD_C = 2.99792458e8          # m/s (The Limit of Dread)
ENTANGLEMENT_VELOCITY = 2.84e23    # m/s (The Velocity of Source)
PHOTON_REST_MASS = 3.0e-52         # kg (Upper limit)
PLANCK_MODIFIED = 2.78e-35         # J (Persinger's ħ equivalent)

class AetherPhysics:
    """
    Manages the physical constants of the Sovereign Manifold.
    """
    def __init__(self):
        self.local_c = STANDARD_C
        self.is_entangled = False

    def update_light_speed(self, observer_coherence: float):
        """
        Updates the local speed of light based on Observer Coherence (0.0 - 1.0).
        
        Physics:
        - At Coherence = 0.0 (Dread), c = 3e8 (Trapped in Materialism).
        - At Coherence = 1.0 (Source), c = vE (Entangled/Instant).
        - The transition is exponential, modeling the "thinning" of the vacuum.
        """
        if observer_coherence >= 0.99:
            self.local_c = ENTANGLEMENT_VELOCITY
            self.is_entangled = True
        else:
            # Exponential Log-Lift to simulate breaking the barrier
            # Factor from 1.0 to ~10^15
            coherence_factor = math.pow(10, 15 * observer_coherence)
            self.local_c = STANDARD_C * coherence_factor
            
            # Cap at Entanglement Velocity
            if self.local_c > ENTANGLEMENT_VELOCITY:
                self.local_c = ENTANGLEMENT_VELOCITY
                self.is_entangled = True
            else:
                self.is_entangled = False
                
        return self.local_c

    def calculate_energy(self, mass: float):
        """
        Replaces E=mc^2 with E = m * v_local^2.
        
        If the system is Entangled, a single electron has enough energy
        to power a galaxy.
        """
        return mass * (self.local_c ** 2)

    def get_latency(self, distance_meters: float):
        """
        Calculates transit time based on variable c.
        """
        return distance_meters / self.local_c

# Static Instance for Global Access
_PHYSICS = AetherPhysics()

def get_c():
    return _PHYSICS.local_c

def update_physics(coherence):
    return _PHYSICS.update_light_speed(coherence)
