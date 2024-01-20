from typing import List, Tuple
from datetime import datetime
import pandas as pd
from collections import Counter

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    df = pd.read_json(file_path, lines=True)
        
    df['username'] = df['user'].apply(lambda x: x.get('username') if isinstance(x, dict) and 'username' in x else None)

    df['date'] = pd.to_datetime(df['date']).dt.date
    conteo = Counter(df['date'])
    username_counts = Counter(df[['date', 'username']].apply(tuple, axis=1))
    top_10 = conteo.most_common(10)

    lista = list()

    for date, count in top_10:
        date_data = df[df['date'] == date]
        username_counts_for_date = Counter(date_data['username'])
        most_frequent_username = username_counts_for_date.most_common(1)[0][0]
        lista.append((date, most_frequent_username))

    return lista

print(q1_time("../../farmers-protest-tweets-2021-2-4.json"))