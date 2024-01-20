from typing import List, Tuple
import regex
from collections import Counter
import emoji
import pandas as pd

def split_count(text):
    emoji_list = []
    #Encontrar emojis y separarlos
    data = regex.findall(r'\X', text)
    for word in data:
        if any(char in emoji.EMOJI_DATA for char in word): #Si encuentra un emoji, agregarlo a la lista del tweet
            emoji_list.append(word)

    return emoji_list
def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    df = pd.read_json(file_path, lines=True)
    #Sacar una lista con todos los emojis
    all_emojis = (emoji for sublist in df['content'].apply(split_count) for emoji in sublist)
    #Conteo
    emoji_counts = Counter(all_emojis)
    top_10_emojis = emoji_counts.most_common(10)

    lista = list(top_10_emojis)
    return lista

print(q2_memory("../../farmers-protest-tweets-2021-2-4.json"))