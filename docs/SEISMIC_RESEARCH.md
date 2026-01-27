# Research: Seismic Photon Prediction (Persinger 2015)

**Directive**: Background photon emissions ($5 \times 10^{-11} \text{ W/m}^2$) spike 2 weeks before major ($M \ge 7.7$) earthquakes.

## 1. The Pre-Seismic Spike
*   **Baseline**: ~50 Units ($5 \times 10^{-11} \text{ W/m}^2$).
*   **Signal**: Increase of +2 to +4 units (sometimes +50) occurs **14 days** before the event.
*   **Global Scope**: The sensor detects events *anywhere* on the planet (Non-local / Global Entanglement).

## 2. Energetic Equivalence
*   **Global Seismic Energy**: $\sim 3.2 \times 10^{15} \text{ J/day}$.
*   **Global Photon Energy**: $\sim 5.57 \times 10^{15} \text{ J/day}$.
*   **Conclusion**: There is an equipartition of energy between Tectonic Stress and Background Light.

## 3. Spectral Periodicities
*   **Major**: 150d, 60d, 30d, 25d.
*   **Recondite**: 18d, 14d, 4-6 days (mean 4.8d), 3 days.

## Implementation Plan (`seismic_prediction.py`)
1.  **`PhotonSensor`**: Simulate the PMT (Photomultiplier Tube) input.
2.  **`SeismicCorrelator`**: Buffer 14 days of data. Look for the +3 Unit deviation.
3.  **`GlobalMonitor`**: Compare modeled "Total Photon Energy" vs "Total Seismic Energy".
