import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    count = employee.groupby('managerId', as_index=False).agg(count=('managerId', 'count')).query('count >= 5')['managerId']
    return employee[employee['id'].isin(count)][['name']]