# Music Recommender Scoring Rule

## Closeness-Based Energy Scoring Function

To reward songs that match the user's preferred energy level (rather than simply favoring higher or lower energy), we use a **Gaussian proximity scoring function**:

```
Score(energy) = e^(-(energy - preferred_energy)² / (2 × σ²))
```

Where:
- `energy`: Song's energy value (0.0 to 1.0 from dataset)
- `preferred_energy`: User's ideal energy level (0.0 to 1.0)
- `σ` (sigma): Controls sensitivity to deviation from preference
  - Smaller σ = stricter matching (sharp peak)
  - Larger σ = more tolerant matching (broad peak)

## Properties
- Maximum score of 1.0 when `energy = preferred_energy`
- Score decreases symmetrically as energy deviates from preference
- Score approaches 0.0 for large deviations
- Naturally normalized between 0 and 1

## Example Calculation

Assume user prefers moderately energetic music: `preferred_energy = 0.6`
Choose `σ = 0.15` for moderate sensitivity

Using song data:
1. Sunrise City: energy=0.82
   - Deviation = |0.82 - 0.6| = 0.22
   - Score = e^(-(0.22)² / (2 × 0.15²)) = e^(-0.0484 / 0.045) = e^(-1.076) ≈ 0.34

2. Midnight Coding: energy=0.42
   - Deviation = |0.42 - 0.6| = 0.18
   - Score = e^(-(0.18)² / (2 × 0.15²)) = e^(-0.0324 / 0.045) = e^(-0.72) ≈ 0.49

3. Gym Hero: energy=0.93
   - Deviation = |0.93 - 0.6| = 0.33
   - Score = e^(-(0.33)² / (2 × 0.15²)) = e^(-0.1089 / 0.045) = e^(-2.42) ≈ 0.09

4. Library Rain: energy=0.35
   - Deviation = |0.35 - 0.6| = 0.25
   - Score = e^(-(0.25)² / (2 × 0.15²)) = e^(-0.0625 / 0.045) = e^(-1.39) ≈ 0.25

## Results Ranking
1. Midnight Coding (0.49) - closest to preference
2. Sunrise City (0.34)
3. Library Rain (0.25)
4. Gym Hero (0.09) - farthest from preference

This scoring approach ensures songs with energy levels nearest to the user's preference receive the highest recommendations, regardless of whether that preference is for high, medium, or low energy music. The σ parameter can be tuned based on how strictly the user wants to match their preferred energy level.