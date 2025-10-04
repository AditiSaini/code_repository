# Import your libraries
import pandas as pd

# Find the best selling item for each month 
online_retail['month'] = online_retail['invoicedate'].dt.month
online_retail['total_paid'] = online_retail['unitprice']*online_retail['quantity']
online_retail = online_retail.groupby(by=['stockcode', 'month'], as_index=False).agg({'invoiceno': 'count', 'total_paid': 'sum', 'description': 'first'})
online_retail['count']=online_retail['invoiceno']
best_item_month = online_retail.groupby(by=['month'], as_index=False)['total_paid'].max()
best_item_month = best_item_month.merge(online_retail, on=['month','total_paid'])[['month', 'description', 'total_paid']]

#Link: https://platform.stratascratch.com/coding/10172-best-selling-item