# Import your libraries
import pandas as pd

#Filter dataset for 2 years 
car_launches = car_launches[car_launches['year'].isin([2019,2020])]
#Number of products launched by company grouped by year 
car_launches_per_year = car_launches.groupby(by=['company_name', 'year'], as_index=False).count()
#Separate data for 2019 and 2020
car_launches_per_year_2019 = car_launches_per_year[car_launches_per_year['year'].isin([2019])]
car_launches_per_year_2020 = car_launches_per_year[car_launches_per_year['year'].isin([2020])]
#Merge both the tables
car_launches_per_year_together = car_launches_per_year_2019.merge(car_launches_per_year_2020, on='company_name')
#Get the net difference
car_launches_per_year_together['net_new_products'] = car_launches_per_year_together['product_name_y']-car_launches_per_year_together['product_name_x']
car_launches_per_year_together = car_launches_per_year_together[['company_name','net_new_products']]
car_launches_per_year_together.head()

#Link: https://platform.stratascratch.com/coding/10318-new-products