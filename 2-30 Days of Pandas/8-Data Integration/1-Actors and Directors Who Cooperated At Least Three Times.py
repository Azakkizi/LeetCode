import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    result = actor_director.groupby(['actor_id', 'director_id'])['timestamp'].count().reset_index()
    return result[result['timestamp'] >= 3][['actor_id', 'director_id']]