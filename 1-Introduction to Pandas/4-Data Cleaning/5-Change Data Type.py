import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    return students.assign(grade=students['grade'].astype(int))
    # OR
    df = pd.DataFrame(students)
    df["grade"] = df[["grade"]].astype(int)
    return df