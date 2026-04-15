# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

**EnergyMatch‑Recommender 1.0** – a simple music recommender that ranks songs by how closely their energy level matches a user‑specified preferred energy, using a Gaussian proximity function.  

---

## 2. Intended Use

The EnergyMatch‑Recommender suggests a short list of songs that best fit a listener’s desired energy level (e.g., “I want upbeat music” or “I need something calm”). It is geared toward students and hobbyists exploring recommendation concepts, not for production deployment. The system assumes the user can articulate a preferred energy value between 0.0 and 1.0 and optionally a favorite genre and mood.

---

## 3. How the Model Works

Each song in the catalog carries an **energy** value (0 = very calm, 1 = very intense). The user supplies a **preferred energy** and optionally a favorite genre and mood. The recommender computes a **Gaussian proximity score**:

```
score = exp(-(energy − preferred_energy)² / (2 × σ²))
```

With a default σ = 0.15, the score is highest (1.0) when the song’s energy matches the user’s preference and falls off symmetrically as the gap grows. After scoring all songs, we sort them descending. If a song also matches the user’s genre or mood, we add a short explanation that highlights those matches, which can tip the ranking when energy scores are close.

Compared to the starter code, we replaced a simplistic “return first k songs” stub with this mathematically‑grounded energy matching and added explanatory text for genre and mood alignment.

---

## 4. Data

The recommender uses the small CSV file **data/songs.csv**, which contains 10 songs. The catalog covers a variety of genres (pop, lofi, rock, ambient, jazz, synthwave, indie pop) and moods (happy, chill, intense, relaxed, moody, focused). Each entry provides numeric attributes such as energy, tempo, valence, danceability, and acousticness.

The dataset was not altered – we kept the original songs to keep the simulation simple. Because it is tiny and genre‑focused, many real‑world listening patterns (e.g., classical, folk, hip‑hop) are missing, limiting the recommender’s ability to generalize beyond the provided styles.

---

## 5. Strengths

- **Energy‑focused users** get intuitive rankings: high‑energy listeners receive upbeat tracks, and low‑energy listeners see calm songs.
- The Gaussian scoring provides a smooth, normalized ranking that gracefully de‑grades as songs move away from the target energy.
- Simple explanations (genre/mood matches) make the recommendations transparent and easy to understand.
- The implementation runs instantly on a tiny catalog, making it ideal for classroom demos and rapid prototyping.

---

## 6. Limitations and Bias

- **Single‑feature focus:** Only energy drives the primary score; genre, mood, and other musical attributes are secondary, so songs with mismatched style can still rank high if their energy aligns.
- **Small catalog bias:** With only 10 songs, any genre or mood that appears few times dominates the results, and the model cannot recommend unseen styles.
- **No diversity enforcement:** The top‑N list may contain very similar tracks, leading to a monotonous listening experience.
- **User input granularity:** Asking users to provide an exact numeric energy value is unrealistic for most listeners.
- **Potential over‑emphasis on genre matches:** When energy scores are close, a genre match can outweigh a larger energy discrepancy, which may unintentionally favor popular genres in the data.  

---

## 7. Evaluation

We evaluated the recommender by running it on three handcrafted user profiles:

1. **High‑Energy Pop** – prefers pop genre, happy mood, and very high energy (0.9).
2. **Chill Lofi** – prefers lofi genre, chill mood, and low energy (0.3).
3. **Deep Intense Rock** – prefers rock genre, intense mood, and high energy (0.9).

For each profile we inspected the top‑5 recommended songs and checked:
- Whether the genre and mood matched the profile.
- How the energy proximity score ordered songs.
- The textual explanations produced by the system.

**Surprises:**
- The *Chill Lofi* profile sometimes returned a pop song with low energy because the Gaussian score dominates over genre when the energy match is strong.
- The *Deep Intense Rock* profile highlighted a rock song with slightly lower energy (0.91) over a pop song with perfect energy match, showing the genre bonus can outweigh a small energy difference.
- Overall, the system behaved as expected: energy proximity drives the ranking, but matching genre/mood adds extra explanation weighting, which can tip close scores.

These informal checks confirmed the Gaussian scoring works and gave insight into how genre and mood cues interact with energy similarity.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection

**Biggest learning moment:** Implementing a Gaussian proximity model taught me how a simple mathematical function can turn a user’s abstract energy preference into a concrete, normalized score that drives recommendations.

**Role of AI tools:** I used the OpenCode assistant (gpt‑oss‑120b) to scaffold code, generate documentation, and suggest edits. I always double‑checked the generated code by running the program and unit tests to ensure correctness.

**Surprise about simple algorithms:** Even with only an energy score, the system sometimes gave high rankings to songs from very different genres, revealing that genre/mood cues are needed to prevent misleading “good” recommendations.

**Next steps:** Extend the scoring to combine energy proximity with weighted genre and mood matches, and experiment with diversity‑enhancing re‑ranking to avoid overly homogeneous top‑N lists.  
