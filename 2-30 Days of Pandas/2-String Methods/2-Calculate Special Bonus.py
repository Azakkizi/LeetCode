import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees["bonus"] = 0
    employees.loc[((~employees["name"].str.startswith('M')) & (employees["employee_id"] % 2 != 0)), "bonus"] = employees["salary"]
    return employees[["employee_id", "bonus"]].sort_values(by="employee_id", ascending=True)