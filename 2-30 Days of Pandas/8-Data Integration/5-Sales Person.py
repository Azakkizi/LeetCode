import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    drop = company.merge(orders, on='com_id').query('name == "RED"')['sales_id']
    result = sales_person[~sales_person.sales_id.isin(drop)][['name']]
    return result