import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    cnt = courses.groupby('class')['student'].count().reset_index()
    return cnt[cnt['student'] >= 5][['class']]