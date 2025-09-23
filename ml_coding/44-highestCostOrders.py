# Import your libraries
import pandas as pd

# Start writing code
aggregated_orders = orders.merge(customers, left_on='cust_id', right_on='id')[['cust_id', 'order_date', 'total_order_cost', 'first_name']]
filtered_orders = aggregated_orders[(aggregated_orders['order_date']>='2019-02-01')&(aggregated_orders['order_date']<='2019-05-01')]
filtered_orders['max_cost'] = (
    filtered_orders
    .groupby(['cust_id','order_date'])['total_order_cost']
    .transform('sum')
)
final_df = filtered_orders.groupby(['order_date'])['max_cost'].max()
merged_df = filtered_orders.merge(final_df, on=['order_date', 'max_cost'])
merged_df = merged_df[['first_name', 'order_date', 'max_cost']].drop_duplicates()

#Link: https://platform.stratascratch.com/coding/9915-highest-cost-orders