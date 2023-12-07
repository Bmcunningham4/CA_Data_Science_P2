import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt

salary_df = pd.read_csv("Salary.csv")
male_df = salary_df[salary_df.Gender == "Male"]
female_df = salary_df[salary_df.Gender == "Female"]

male_UK_mean = round(male_df[male_df.Country == "UK"].Salary.mean(), 2)
male_USA_mean = round(male_df[male_df.Country == "USA"].Salary.mean(), 2)
male_Canada_mean = round(male_df[male_df.Country == "Canada"].Salary.mean(), 2)
male_China_mean = round(male_df[male_df.Country == "China"].Salary.mean(), 2)
male_Australia_mean = round(male_df[male_df.Country == "Australia"].Salary.mean(), 2)

female_UK_mean = round(female_df[female_df.Country == "UK"].Salary.mean(), 2)
female_USA_mean = round(female_df[female_df.Country == "USA"].Salary.mean(), 2)
female_Canada_mean = round(female_df[female_df.Country == "Canada"].Salary.mean(), 2)
female_China_mean = round(female_df[female_df.Country == "China"].Salary.mean(), 2)
female_Australia_mean = round(female_df[female_df.Country == "Australia"].Salary.mean(), 2)

uk_mean_diff = male_UK_mean - female_UK_mean
USA_mean_diff = male_USA_mean - female_USA_mean
Canada_mean_diff = male_Canada_mean - female_Canada_mean
China_mean_diff = male_China_mean - female_China_mean
Australia_mean_diff = male_Australia_mean - female_Australia_mean

#todo: I don't feel like doing this now but after the bar graphs..
#! order & and check my updated notes on what to do from here..
print(round(Canada_mean_diff))
print(round(USA_mean_diff))
print(round(uk_mean_diff))
print(round(Australia_mean_diff))
print(round(China_mean_diff))
