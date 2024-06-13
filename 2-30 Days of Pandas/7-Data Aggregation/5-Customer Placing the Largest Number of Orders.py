import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    return orders['customer_number'].mode().to_frame()
    # OR
    ord_cnt = orders.groupby('customer_number')['order_number'].count().reset_index()
    return ord_cnt[ord_cnt['order_number'] == ord_cnt['order_number'].max()][['customer_number']]