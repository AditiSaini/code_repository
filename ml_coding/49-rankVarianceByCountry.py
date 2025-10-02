# Import your libraries
import pandas as pd

fb_users_comments = fb_comments_count.merge(fb_active_users[['user_id', 'country']], on='user_id')
fb_users_comments = fb_users_comments[(fb_users_comments['created_at']>='2019-12-01') & (fb_users_comments['created_at']<='2020-01-31')]
fb_users_comments['month'] = fb_users_comments['created_at'].dt.month
fb_users_comments['year'] = fb_users_comments['created_at'].dt.year
fb_users_comments = fb_users_comments.groupby(by=['year', 'month', 'country'], as_index=False)['number_of_comments'].sum()
fb_users_comments['rank'] = fb_users_comments.groupby(by=['year', 'month'])['number_of_comments'].rank('dense', ascending=False)
countries_with_improved_rank = fb_users_comments.pivot(index=['country'], columns='year', values='rank').reset_index()
countries_with_improved_rank['diff'] = countries_with_improved_rank[2019]-countries_with_improved_rank[2020]
improved_countries = countries_with_improved_rank[countries_with_improved_rank['diff']>0]['country']

#Link: https://platform.stratascratch.com/coding/2007-rank-variance-per-country