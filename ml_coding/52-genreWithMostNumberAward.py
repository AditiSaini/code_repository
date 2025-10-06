# Import your libraries
import pandas as pd

oscar_nominees = oscar_nominees[oscar_nominees['winner']==True]
oscar_nominees = oscar_nominees.groupby(by=['nominee'], as_index=False)['winner'].count().sort_values('winner', ascending=False).sort_values(by='nominee')
oscar_nominees = oscar_nominees[oscar_nominees['winner']==max(oscar_nominees['winner'])]
oscar_nominees = oscar_nominees.merge(nominee_information, left_on='nominee', right_on='name')['top_genre']

#Link: https://platform.stratascratch.com/coding/10171-find-the-genre-of-the-person-with-the-most-number-of-oscar-winnings