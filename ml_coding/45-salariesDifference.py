# Import your libraries
import pandas as pd

dept_id_marketing = int(db_dept[(db_dept['department']=='marketing')]['id'])
dept_id_engineering = int(db_dept[(db_dept['department']=='engineering')]['id'])

max_salary_marketing = int(db_employee[db_employee['department_id']==dept_id_marketing].sort_values(by='salary', ascending=False).head(1)['salary'])
max_salary_engineering = int(db_employee[db_employee['department_id']==dept_id_engineering].sort_values(by='salary', ascending=False).head(1)['salary'])
pd.DataFrame({'salary_difference': [abs(max_salary_marketing-max_salary_engineering)]})

#Link: https://platform.stratascratch.com/coding/10308-salaries-differences