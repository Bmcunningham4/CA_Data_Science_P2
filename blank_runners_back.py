import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
import re

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





#? This crap is separate but includes the 25 job titles that the boolean doesn't catch
def job_title_funct(title):
    tech_keywords = re.compile(r'\bsoftware\b|\bdeveloper\b|\bengineer\b|\bit|\bdata\b', flags=re.IGNORECASE)
    manager_keywords = re.compile(r'\bmanager\b|\bdirector\b|\bceo\b|\bvp|\boperations\b', flags=re.IGNORECASE)
    marketing_keywords = re.compile(r'\bmarketing\b|\banalyst\b|\bcoordinator\b|\bspecialist|\bdigital\b', flags=re.IGNORECASE)
    finance_keywords = re.compile(r'\bfinancial\b|\banalyst\b|\baccountant\b|\badvisor|\bintelligence\b', flags=re.IGNORECASE)
    creative_keywords = re.compile(r'\bdesigner\b|\bcreative\b|\bcontent\b|\bgraphic|\bux\b', flags=re.IGNORECASE)
    
    if any(re.search(tech_keywords, title) for title in [title]):
        return "Technology"
    elif any(re.search(manager_keywords, title) for title in [title]):
        return "Management"
    elif any(re.search(marketing_keywords, title) for title in [title]):
        return "Marketing"
    elif any(re.search(finance_keywords, title) for title in [title]):
        return "Finance"
    elif any(re.search(creative_keywords, title) for title in [title]):
        return "Creative"
    else:
        return title  # Returning the title itself for uncategorized titles

# Assuming salary_df is your DataFrame containing job titles and salaries
salary_df["Job Type"] = salary_df["Job Title"].apply(job_title_funct)

# Extracting and printing unique uncategorized job titles
uncategorized_titles = salary_df[salary_df["Job Type"] == salary_df["Job Title"]]["Job Title"].unique()
print("Uncategorized Job Titles:")
print(len(uncategorized_titles))
for job in uncategorized_titles:
    print(job)
