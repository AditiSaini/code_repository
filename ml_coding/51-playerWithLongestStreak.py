# Import your libraries
import pandas as pd

players_results.sort_values(by=['player_id', 'match_date'])
players_results['streak_id'] = (players_results['match_result'] != players_results['match_result'].shift()).cumsum()
players_results = players_results[players_results["match_result"] == "W"]
players_results = players_results[['player_id', 'streak_id', 'match_date']].groupby(["player_id", "streak_id"]).count().reset_index()
players_results = players_results.groupby(["player_id"]).max().reset_index()
max_streak = max(players_results['match_date'])
players_results = players_results[players_results['match_date']==max_streak][['player_id', 'match_date']]

#Link: https://platform.stratascratch.com/coding/2059-player-with-longest-streak