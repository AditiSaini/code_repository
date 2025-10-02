# Import your libraries
import pandas as pd

all_actors = pd.DataFrame(actor_rating_shift['actor_name'].drop_duplicates())
actor_rating_shift['rank'] = actor_rating_shift.groupby(by=['actor_name'], as_index=False)['release_date'].rank('first', ascending=False)
actor_latest_release = all_actors.merge(actor_rating_shift[actor_rating_shift['rank']==1], on='actor_name', how='left').fillna(0)
actor_history = all_actors.merge(actor_rating_shift[actor_rating_shift['rank']!=1], on='actor_name', how='left').fillna(0)
actor_history_avg = actor_history.groupby('actor_name', as_index=False)['film_rating'].mean()
actor_history_avg['avg_rating'] = actor_history_avg['film_rating']
actor_history_avg = actor_history_avg.merge(actor_latest_release, on='actor_name')
actor_rating_diff = actor_history_avg[['actor_name', 'avg_rating', 'film_rating_y']]
actor_rating_diff['rating_difference'] = actor_rating_diff['film_rating_y']-actor_rating_diff['avg_rating']
actor_rating_shift = actor_rating_diff

#Link: https://platform.stratascratch.com/coding/10547-actor-rating-difference-analysis