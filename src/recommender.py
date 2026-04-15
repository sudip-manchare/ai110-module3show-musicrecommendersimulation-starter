from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import math

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return the top *k* songs sorted by relevance score.

        Relevance is currently computed using a Gaussian proximity function on the
        song's ``energy`` attribute relative to the user's ``target_energy``.
        A default ``sigma`` of 0.15 provides a reasonable tolerance.
        """
        sigma = 0.15
        def gaussian_score(song: Song) -> float:
            diff = song.energy - user.target_energy
            return math.exp(-(diff ** 2) / (2 * sigma ** 2))
        # Compute scores and sort descending
        scored = [(song, gaussian_score(song)) for song in self.songs]
        scored.sort(key=lambda pair: pair[1], reverse=True)
        return [song for song, _ in scored[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Explain why *song* was recommended to *user*.

        The explanation focuses on the energy proximity score and notes when the
        song matches the user's favorite genre or mood.
        """
        sigma = 0.15
        diff = song.energy - user.target_energy
        energy_score = math.exp(-(diff ** 2) / (2 * sigma ** 2))
        parts = []
        # Energy component
        parts.append(f"energy proximity score {energy_score:.2f}")
        # Genre match
        if song.genre == user.favorite_genre:
            parts.append("matches favorite genre")
        # Mood match
        if song.mood == user.favorite_mood:
            parts.append("matches favorite mood")
        # Acoustic preference
        if user.likes_acoustic:
            parts.append(f"acousticness {song.acousticness:.2f}")
        return ", ".join(parts)

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from *csv_path* and return a list of dictionaries.

    Each row is converted to appropriate Python types (int, float, str).
    """
    import csv
    songs: List[Dict] = []
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Convert numeric fields
            song = {
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            }
            songs.append(song)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score *song* for *user_prefs*.

    Returns a tuple ``(score, reasons)`` where ``score`` is the Gaussian
    proximity score based on energy and ``reasons`` is a list of human‑readable
    explanations (genre match, mood match, acoustic preference).
    """
    sigma = 0.15
    # Energy proximity score
    diff = song["energy"] - user_prefs.get("energy", 0.5)
    energy_score = math.exp(-(diff ** 2) / (2 * sigma ** 2))
    reasons: List[str] = [f"energy proximity {energy_score:.2f}"]
    # Genre match
    if song.get("genre") == user_prefs.get("genre"):
        reasons.append("matches favorite genre")
    # Mood match
    if song.get("mood") == user_prefs.get("mood"):
        reasons.append("matches favorite mood")
    # Acoustic preference (optional flag)
    if user_prefs.get("likes_acoustic"):
        reasons.append(f"acousticness {song.get('acousticness'):.2f}")
    return energy_score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Return the top *k* songs for *user_prefs*.

    Each result is a tuple ``(song_dict, score, explanation)`` where ``score``
    is the Gaussian energy proximity score and ``explanation`` concatenates the
    reason strings returned by :func:`score_song`.
    """
    # Compute scores and explanations for all songs
    scored: List[Tuple[Dict, float, List[str]]] = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        scored.append((song, score, reasons))
    # Sort descending by score
    scored.sort(key=lambda tup: tup[1], reverse=True)
    # Prepare final list
    top = []
    for song, score, reasons in scored[:k]:
        explanation = ", ".join(reasons)
        top.append((song, score, explanation))
    return top
