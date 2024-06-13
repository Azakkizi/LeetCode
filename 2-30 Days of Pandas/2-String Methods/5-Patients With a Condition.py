import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    return patients[patients["conditions"].apply(lambda x: any([c.startswith('DIAB1') for c in x.split()]))]