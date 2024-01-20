from typing import List, Tuple
import regex
from collections import Counter
import emoji
import pandas as pd

def split_count(text):
    return [char for char in regex.findall(r'\X', text) if char in emoji.EMOJI_DATA]

def q2_time(file_path: str) -> List[Tuple[str, int]]:
    df = pd.read_json(file_path, lines=True)
    
    emoji_lists = df['content'].apply(split_count)
    all_emojis = [emoji for sublist in emoji_lists for emoji in sublist]
    emoji_counts = Counter(all_emojis)
    top_10_emojis = emoji_counts.most_common(10)

    lista = [(emoji, count) for emoji, count in top_10_emojis]

    return lista

print(q2_time("../../farmers-protest-tweets-2021-2-4.json"))