## Profile Comparisons

### High‑Energy Pop vs Chill Lofi
- **Energy scores:** The Pop profile (energy 0.9) heavily favors songs near 0.9, while the Lofi profile (energy 0.3) gives high scores to low‑energy tracks. Consequently, the same song can rank high for one profile and low for the other depending on its energy.
- **Genre influence:** When a low‑energy pop song appears, the Pop profile still ranks it higher because the genre match adds explanation weight, but the Lofi profile may still prefer a lofi track with a slightly higher energy if the genre bonus outweighs the energy gap.
- **Makes sense:** Energy is the dominant factor; genre/mood are secondary cues that can shift close scores.

### High‑Energy Pop vs Deep Intense Rock
- **Genre vs energy trade‑off:** Both profiles want high energy (≈0.9). The Rock profile also requires genre = "rock". A rock song with energy 0.91 outranks a pop song with perfect energy 0.9 because the genre match adds a matching‑genre reason, illustrating that the system combines energy proximity with genre/mood cues.
- **Mood match:** Both profiles also specify moods (happy vs intense). When mood aligns, it further boosts the explanation, reinforcing the ranking.
- **Interpretation:** The system correctly balances energy proximity with categorical matches.

### Chill Lofi vs Deep Intense Rock
- **Opposite energy preferences:** Lofi prefers low energy (0.3) while Rock prefers high energy (0.9). The same song will receive opposite scores, demonstrating the Gaussian function’s symmetry.
- **Genre dominance:** Even if a song’s energy is moderate, the matching genre can pull it into the top‑5 for the corresponding profile, which is why a low‑energy lofi track can appear for the Lofi profile despite a modest energy match.
- **Why it makes sense:** The Gaussian scoring ensures that energy distance is the primary driver, but genre/mood tags act as tie‑breakers, leading to intuitive differences between the two extreme profiles.
