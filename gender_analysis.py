
#? This file will contain:
"""
Gender Pay Gap Analysis:
Explore salary differences between genders across:
- different job titles, 
- countries
- seniority levels. 

#* Most importantly
Identify if there's a significant gap and in what contexts it's most prominant!
"""

# Little note for learning what granularity means in data:
"""
High granularity basically means very detailed and includes things like every transaction in a retail store, or temperature readings from different sensors every second
Low Granularity means the opposite and includes things like only the monthly sails for a retail store or Annual average temp..

High granularity can potenitally go into deeper analysis but can sometimes be overwhelming or too hard to extract insights from..
Low Granularity can be good sometimes easier to manage and manipulate but can't lead to as deep insights or analysis...
"""

#? There isn't much to know about cleaning and checking data from what I could find:
#? So without further adue, let's begin your analysis benno...

import pandas as pd
import numpy as np
import seaborn as sns
import csv
#? Only other shite I'll have to import is the skits. stats crap..

salary_df = pd.read_csv("Salary.csv")
print(salary_df.head(), '\n') #---- data looks good doesn't even look like it needs any cleaning...

#! Start of basic info summary, and what I'm measuring:
"""
Mean 
Median
Range & Variance
Visualization of these ^^
(Then I'll get to more specific areas after )
"""

#! mean
#* Most basic: Avg salary for male/ female no context!
mean_female_salary = salary_df[salary_df["Gender"] == "Female"].Salary.mean() #* I just realised I actually don't know what currency I'm dealing with in here!!
mean_male_salary = salary_df[salary_df["Gender"] == "Male"].Salary.mean()

print(f"The average male salary is ${round(mean_male_salary, 2)}")
print(f"The average female salary is ${round(mean_female_salary, 2)}")
mean_salary_diff = round(mean_male_salary - mean_female_salary,2)

print(f"The mean salary difference is + ${mean_salary_diff} towards the male", '\n')


#! Median
median_female_salary = salary_df[salary_df["Gender"] == "Female"].Salary.median() 
median_male_salary = salary_df[salary_df["Gender"] == "Male"].Salary.median()

print(f"The median male salary is ${round(median_male_salary, 2)}")
print(f"The median female salary is ${round(median_female_salary, 2)}")
mean_salary_diff = round(median_male_salary - median_female_salary,2)

print(f"The median salary difference is + ${mean_salary_diff} towards the male", '\n')





