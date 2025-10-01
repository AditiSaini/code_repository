# Import your libraries
import pandas as pd

sf_events = sf_events.sort_values(by='record_date')[['record_date', 'user_id']].drop_duplicates()
sf_events['rank'] = sf_events.groupby('user_id')['record_date'].rank('first', ascending=True)
sf_events['consecutive_days'] = sf_events['record_date'] - pd.to_timedelta(sf_events['rank'], unit='D')
active_user_consec_days = sf_events.groupby(by=['user_id', 'consecutive_days'], as_index=False)['record_date'].count()
filtered_active_users = active_user_consec_days[active_user_consec_days['record_date']>=3][['user_id']]
filtered_active_users.head()

#Link: https://platform.stratascratch.com/coding/2054-consecutive-days