import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#todo: When I come back!
#! Stop sooking about VSC until this project is done and then sort next wk!
#? Then Fix this boxplot crap myself don't waste more time getting chat to do it, it overcomplicates something very simple!
#? Have a much better crack at getting this data viz happening goat..

salary_df = pd.read_csv("Salary.csv")
#* just realised I dont actually need to separarat these guys! But don't forget this copy business!!
male_df = salary_df[salary_df.Gender == "Male"].copy() #* Take note of this I have to use .copy() method as I was getting a warning about chained indexing since I was trying to make changes not to the original dataframe but a new one which was a version of old...
female_df = salary_df[salary_df.Gender == "Female"].copy()

#? Not Creating new dataframes this time!
def age_group_funct(age):
    if 19 < age < 30:
        return "20 - 29"
    elif 29 <  age < 40:
        return "30 - 39"
    elif 39 < age < 50:
        return "40 - 49"
    else:
        return '50+'

male_df["Age Group"] = male_df.Age.apply(age_group_funct)
female_df["Age Group"] = female_df.Age.apply(age_group_funct)


#! OHHHHHH okkkk When doing this I don't actually have to make a new 2 column dataframe I just have to select the 2 columns that I want!
age_order = ['20 - 29', '30 - 39', '40 - 49', '50+']

combined_df = pd.concat([male_df, female_df])

# Create boxplots with hue as "Gender"
sns.boxplot(data=combined_df, y="Salary", x="Age Group", order=age_order, hue="Gender") #* Pay attention to this hue guy he's pretty clutch
plt.show()
plt.close()