import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#todo: When I come back!
#! Stop sooking about VSC until this project is done and then sort next wk!
#? Then Fix this boxplot crap myself don't waste more time getting chat to do it, it overcomplicates something very simple!
#? Have a much better crack at getting this data viz happening goat..

salary_df = pd.read_csv("Salary.csv")
male_df = salary_df[salary_df.Gender == "Male"]
female_df = salary_df[salary_df.Gender == "Female"]

#? Data for visualisations! (Important moment here)
male_20_29 = male_df[(male_df.Age > 19) & (male_df.Age <  30)].copy() #* Take note of this I have to use .copy() method as I was getting a warning about chained indexing since I was trying to make changes not to the original dataframe but a new one which was a version of old...
male_30_39 = male_df[(male_df.Age > 29) & (male_df.Age <  40)].copy()
male_40_49 = male_df[(male_df.Age > 39) & (male_df.Age <  50)].copy()
male_50_100 = male_df[(male_df.Age > 49) & (male_df.Age <  100)].copy()

female_20_29 = female_df[(female_df.Age > 19) & (female_df.Age <  30)].copy()
female_30_39 = female_df[(female_df.Age > 29) & (female_df.Age <  40)].copy()
female_40_49 = female_df[(female_df.Age > 39) & (female_df.Age <  50)].copy()
female_50_100 = female_df[(female_df.Age > 49) & (female_df.Age <  100)].copy()

#? New Column to group ages
male_20_29.loc[:, "Age Group"] = "20 - 29"
male_30_39.loc[:, "Age Group"] = "30 - 39"
male_40_49.loc[:, "Age Group"] = "40 - 49"
male_50_100.loc[:, "Age Group"] = "50+"

female_20_29.loc[:, "Age Group"] = "20 - 29"
female_30_39.loc[:, "Age Group"] = "30 - 39"
female_40_49.loc[:, "Age Group"] = "40 - 49"
female_50_100.loc[:, "Age Group"] = "50+"

#! OHHHHHH okkkk When doing this I don't actually have to make a new 2 column dataframe I just have to select the 2 columns that I want!
sns.boxplot(data = male_20_29, x = "Salary", y = "Age Group")
plt.show()
plt.close()