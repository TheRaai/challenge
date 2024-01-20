from typing import List, Tuple
import pandas as pd
from collections import Counter

def sacar_usuarios(mentioned_users):
    if mentioned_users is None:
            return []
    return [user['username'] for user in mentioned_users if user and 'username' in user and user['username'] is not None]



def q3_time(file_path: str) -> List[Tuple[str, int]]:
    df = pd.read_json(file_path, lines=True)
    df = df[['mentionedUsers']]
    conteo = Counter()

    conteo = Counter(df['mentionedUsers'].apply(sacar_usuarios).explode())

    return(conteo.most_common(10))

print(q3_time("../../farmers-protest-tweets-2021-2-4.json"))