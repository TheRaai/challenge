from typing import List, Tuple
from datetime import datetime
from collections import Counter
import pandas as pd
import json


def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    df = pd.read_json(file_path, lines=True)
    df = df[['date','user']]

    # Extraer el usuario de la columna 
    df['username'] = df['user'].apply(lambda x: x.get('username') if isinstance(x, dict) and 'username' in x else None)

    # Pasar a fecha para que no influya la hora
    df['date'] = pd.to_datetime(df['date']).dt.date

    # Contador de usuarios
    username_counts = Counter(df[['date', 'username']].apply(tuple, axis=1))

    # Top 10 de fechas
    top_10 = Counter(df['date']).most_common(10)

    lista = list()

    # Ir viendo top usuario por fecha
    for date, count in top_10:
        date_data = df[df['date'] == date]
        username_counts_for_date = Counter(date_data['username'])
        
        # Encontrar el usuario más frecuente en la fecha
        most_frequent_username = username_counts_for_date.most_common(1)[0][0]
        lista.append((date, most_frequent_username))
    return lista

print(q1_memory("../../farmers-protest-tweets-2021-2-4.json"))