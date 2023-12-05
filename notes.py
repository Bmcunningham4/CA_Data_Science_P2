
#? This is cooked let's see if I can fix this b4 I forget how to tomorrow..
#* Copy and pasting everything here and then re committing after!!

#! AGE
#? WTF I literally just deleted a cell with all my table data and can't get back now...
#! That's so fkd how that can
#* Table data
mean_table = [
    ["Age 20 - 29", male_20_29_mean, female_20_29_mean],
    ["Age 30 - 39", male_30_39_mean, female_30_39_mean],
    ["Age 40 - 49", male_40_49_mean, female_40_49_mean],
    ["Age 50+ ", male_50_100_mean, female_50_100_mean]
]
median_table = [
    ["Age 20 - 29", male_20_29_median, female_20_29_median],
    ["Age 30 - 39", male_30_39_median, female_30_39_median],
    ["Age 40 - 49", male_40_49_median, female_40_49_median],
    ["Age 50+ ", male_50_100_median, female_50_100_median]
]
std_table = [
    ["Age 20 - 29", male_20_29_std, female_20_29_std],
    ["Age 30 - 39", male_30_39_std, female_30_39_std],
    ["Age 40 - 49", male_40_49_std, female_40_49_std],
    ["Age 50+ ", male_50_100_std, female_50_100_std]
]
max_table = [
    ["Age 20 - 29", male_20_29_max, female_20_29_max],
    ["Age 30 - 39", male_30_39_max, female_30_39_max],
    ["Age 40 - 49", male_40_49_max, female_40_49_max],
    ["Age 50+ ", male_50_100_max, female_50_100_max]
]
min_table = [
    ["Age 20 - 29", male_20_29_min, female_20_29_min],
    ["Age 30 - 39", male_30_39_min, female_30_39_min],
    ["Age 40 - 49", male_40_49_min, female_40_49_min],
    ["Age 50+ ", male_50_100_min, female_50_100_min]
]
diff_table = [
    ["Age 20 - 29", male_20_29_diff, female_20_29_diff],
    ["Age 30 - 39", male_30_39_diff, female_30_39_diff],
    ["Age 40 - 49", male_40_49_diff, female_40_49_diff],
    ["Age 50+ ", male_50_100_diff, female_50_100_diff]
]

#* Table creator function
def table_creator(table_data):
    formatted_table_data = []
    headers_list = ["Age Groups", "Male", "Female"]

    for row in table_data:
        formatted_row = []
        for value in row:
            if isinstance(value, (int, float)):
                formatted_value = f"{round(value):,.0f}"  
            elif isinstance(value, str):
                formatted_value = value  
            else:
                formatted_value = str(value)  
            formatted_row.append(formatted_value)
        formatted_table_data.append(formatted_row)

    table = tabulate(formatted_table_data, headers_list, tablefmt="fancy_grid")
    return table

#* Making the tables..
print("Mean Salary Table")
formatted_table = table_creator(mean_table)
print(formatted_table, '\n')

print("Median Salary Table")
formatted_table = table_creator(median_table)
print(formatted_table, '\n')

print("Standard Deviation Table")
formatted_table = table_creator(std_table)
print(formatted_table, '\n')

print("Maximum Salary Table")
formatted_table = table_creator(max_table)
print(formatted_table, '\n')

print("Minimum Salary Table")
formatted_table = table_creator(min_table)
print(formatted_table, '\n')

print("Salary Range Table")
formatted_table = table_creator(diff_table)
print(formatted_table, '\n')

#! basic_data 
#todo: I think this is the part where I should format the values so their more readable!!!
table_data = [
    ["Mean", mean_male_salary, mean_female_salary],
    ["Median", median_male_salary, median_female_salary],
    ["STD", std_male_salary, std_female_salary],
    ["Max", max_male_salary, max_female_salary],
    ["Min", min_male_salary, min_female_salary],
    ["Range", range_male_salary, range_female_salary]
]

table_headers = ["Salary Metrics", "Male", "Female"]
table = tabulate(table_data, table_headers, tablefmt="fancy_grid")
print(table)

formatted_table_data = []  

for row in table_data:
    formatted_row = []
    for value in row:
        if isinstance(value, (int, float)):
            formatted_value = f"{value:,.2f}"
        elif isinstance(value, str):
            formatted_value = value  
        else:
            formatted_value = str(value)  
        formatted_row.append(formatted_value)
    formatted_table_data.append(formatted_row)  

table_headers = ["Salary Metrics", "Male", "Female"]
table = tabulate(formatted_table_data, table_headers, tablefmt="fancy_grid")
print(table)

formatted_table_data = []

for row in table_data:
    formatted_row = []
    for value in row:
        if isinstance(value, (int, float)):
            formatted_value = f"${round(value):,.0f}"  # Round to nearest whole number and add $ sign
        elif isinstance(value, str):
            formatted_value = value  
        else:
            formatted_value = str(value)  
        formatted_row.append(formatted_value)
    formatted_table_data.append(formatted_row)

table_headers = ["Salary Metrics", "Male", "Female"]
table = tabulate(formatted_table_data, table_headers, tablefmt="fancy_grid")

print(table)


#todo: Will have to check which form is best practice to write and I think it would be good to have these all on 1 page with a title in between
#? And I could have the formatted data on their respective files then import all that data to the tables file...

#! country

#* Table data
mean_table = [
    ["UK", male_UK_mean, female_UK_mean],
    ["USA", male_USA_mean, female_USA_mean],
    ["Canada", male_Canada_mean, female_Canada_mean],
    ["China", male_China_mean, female_China_mean],
    ["Australia", male_Australia_mean, female_Australia_mean]
]
median_table = [
    ["UK", male_UK_median, female_UK_median],
    ["USA", male_USA_median, female_USA_median],
    ["Canada", male_Canada_median, female_Canada_median],
    ["China", male_China_median, female_China_median],
    ["Australia", male_Australia_median, female_Australia_median]
]
std_table = [
    ["UK", male_UK_std, female_UK_std],
    ["USA", male_USA_std, female_USA_std],
    ["Canada", male_Canada_std, female_Canada_std],
    ["China", male_China_std, female_China_std],
    ["Australia", male_Australia_std, female_Australia_std]
]
min_table = [
    ["UK", male_UK_min, female_UK_min],
    ["USA", male_USA_min, female_USA_min],
    ["Canada", male_Canada_min, female_Canada_min],
    ["China", male_China_min, female_China_min],
    ["Australia", male_Australia_min, female_Australia_min]
]
max_table = [
    ["UK", male_UK_max, female_UK_max],
    ["USA", male_USA_max, female_USA_max],
    ["Canada", male_Canada_max, female_Canada_max],
    ["China", male_China_max, female_China_max],
    ["Australia", male_Australia_max, female_Australia_max]
]
diff_table = [
    ["UK", male_UK_diff, female_UK_diff],
    ["USA", male_USA_diff, female_USA_diff],
    ["Canada", male_Canada_diff, female_Canada_diff],
    ["China", male_China_diff, female_China_diff],
    ["Australia", male_Australia_diff, female_Australia_diff]
]


#* Table creator function
def table_creator(table_data):
    formatted_table_data = []
    headers_list = ["Age Groups", "Male", "Female"]

    for row in table_data:
        formatted_row = []
        for value in row:
            if isinstance(value, (int, float)):
                formatted_value = f"{round(value):,.0f}"  
            elif isinstance(value, str):
                formatted_value = value  
            else:
                formatted_value = str(value)  
            formatted_row.append(formatted_value)
        formatted_table_data.append(formatted_row)

    table = tabulate(formatted_table_data, headers_list, tablefmt="fancy_grid")
    return table

print("Mean Salary Table")
formatted_table = table_creator(mean_table)
print(formatted_table, '\n')

print("Median Salary Table")
formatted_table = table_creator(median_table)
print(formatted_table, '\n')

print("Standard Deviation Table")
formatted_table = table_creator(std_table)
print(formatted_table, '\n')

print("Maximum Salary Table")
formatted_table = table_creator(max_table)
print(formatted_table, '\n')

print("Minimum Salary Table")
formatted_table = table_creator(min_table)
print(formatted_table, '\n')

print("Salary Range Table")
formatted_table = table_creator(diff_table)
print(formatted_table, '\n')

#! Country
#* Table data
mean_table = [
    ["0: High School", male_0_mean, female_0_mean],
    ["1: Bachelor Degree", male_1_mean, female_1_mean],
    ["2: Master Degree", male_2_mean, female_2_mean],
    ["3: Phd", male_3_mean, female_3_mean]
]
median_table = [
    ["0: High School", male_0_median, female_0_median],
    ["1: Bachelor Degree", male_1_median, female_1_median],
    ["2: Master Degree", male_2_median, female_2_median],
    ["3: Phd", male_3_median, female_3_median]
]
std_table = [
    ["0: High School", male_0_std, female_0_std],
    ["1: Bachelor Degree", male_1_std, female_1_std],
    ["2: Master Degree", male_2_std, female_2_std],
    ["3: Phd", male_3_std, female_3_std]
]
min_table = [
    ["0: High School", male_0_min, female_0_min],
    ["1: Bachelor Degree", male_1_min, female_1_min],
    ["2: Master Degree", male_2_min, female_2_min],
    ["3: Phd", male_3_min, female_3_min]
]
max_table = [
    ["0: High School", male_0_max, female_0_max],
    ["1: Bachelor Degree", male_1_max, female_1_max],
    ["2: Master Degree", male_2_max, female_2_max],
    ["3: Phd", male_3_max, female_3_max]
]
diff_table = [
    ["0: High School", male_0_diff, female_0_diff],
    ["1: Bachelor Degree", male_1_diff, female_1_diff],
    ["2: Master Degree", male_2_diff, female_2_diff],
    ["3: Phd", male_3_diff, female_3_diff]
]


#* Table creator function
def table_creator(table_data):
    formatted_table_data = []
    headers_list = ["Education Level", "Male", "Female"]

    for row in table_data:
        formatted_row = []
        for value in row:
            if isinstance(value, (int, float)):
                formatted_value = f"{round(value):,.0f}"  
            elif isinstance(value, str):
                formatted_value = value  
            else:
                formatted_value = str(value)  
            formatted_row.append(formatted_value)
        formatted_table_data.append(formatted_row)

    table = tabulate(formatted_table_data, headers_list, tablefmt="fancy_grid")
    return table

print("Mean Salary Table")
formatted_table = table_creator(mean_table)
print(formatted_table, '\n')

print("Median Salary Table")
formatted_table = table_creator(median_table)
print(formatted_table, '\n')

print("Standard Deviation Table")
formatted_table = table_creator(std_table)
print(formatted_table, '\n')

print("Maximum Salary Table")
formatted_table = table_creator(max_table)
print(formatted_table, '\n')

print("Minimum Salary Table")
formatted_table = table_creator(min_table)
print(formatted_table, '\n')

print("Salary Range Table")
formatted_table = table_creator(diff_table)
print(formatted_table, '\n')

#! education_level
#* Table data
mean_table = [
    ["0: High School", male_0_mean, female_0_mean],
    ["1: Bachelor Degree", male_1_mean, female_1_mean],
    ["2: Master Degree", male_2_mean, female_2_mean],
    ["3: Phd", male_3_mean, female_3_mean]
]
median_table = [
    ["0: High School", male_0_median, female_0_median],
    ["1: Bachelor Degree", male_1_median, female_1_median],
    ["2: Master Degree", male_2_median, female_2_median],
    ["3: Phd", male_3_median, female_3_median]
]
std_table = [
    ["0: High School", male_0_std, female_0_std],
    ["1: Bachelor Degree", male_1_std, female_1_std],
    ["2: Master Degree", male_2_std, female_2_std],
    ["3: Phd", male_3_std, female_3_std]
]
min_table = [
    ["0: High School", male_0_min, female_0_min],
    ["1: Bachelor Degree", male_1_min, female_1_min],
    ["2: Master Degree", male_2_min, female_2_min],
    ["3: Phd", male_3_min, female_3_min]
]
max_table = [
    ["0: High School", male_0_max, female_0_max],
    ["1: Bachelor Degree", male_1_max, female_1_max],
    ["2: Master Degree", male_2_max, female_2_max],
    ["3: Phd", male_3_max, female_3_max]
]
diff_table = [
    ["0: High School", male_0_diff, female_0_diff],
    ["1: Bachelor Degree", male_1_diff, female_1_diff],
    ["2: Master Degree", male_2_diff, female_2_diff],
    ["3: Phd", male_3_diff, female_3_diff]
]


#* Table creator function
def table_creator(table_data):
    formatted_table_data = []
    headers_list = ["Education Level", "Male", "Female"]

    for row in table_data:
        formatted_row = []
        for value in row:
            if isinstance(value, (int, float)):
                formatted_value = f"{round(value):,.0f}"  
            elif isinstance(value, str):
                formatted_value = value  
            else:
                formatted_value = str(value)  
            formatted_row.append(formatted_value)
        formatted_table_data.append(formatted_row)

    table = tabulate(formatted_table_data, headers_list, tablefmt="fancy_grid")
    return table

print("Mean Salary Table")
formatted_table = table_creator(mean_table)
print(formatted_table, '\n')

print("Median Salary Table")
formatted_table = table_creator(median_table)
print(formatted_table, '\n')

print("Standard Deviation Table")
formatted_table = table_creator(std_table)
print(formatted_table, '\n')

print("Maximum Salary Table")
formatted_table = table_creator(max_table)
print(formatted_table, '\n')

print("Minimum Salary Table")
formatted_table = table_creator(min_table)
print(formatted_table, '\n')

print("Salary Range Table")
formatted_table = table_creator(diff_table)
print(formatted_table, '\n')

#! job_titles
#* Table data
mean_table = [
    ["Technology", male_technology_mean, female_technology_mean],
    ["Management", male_management_mean, female_management_mean],
    ["Marketing", male_marketing_mean, female_marketing_mean],
    ["Finance", male_finance_mean, female_finance_mean],
    ["Creative", male_creative_mean, female_creative_mean]
]
median_table = [
    ["Technology", male_technology_median, female_technology_median],
    ["Management", male_management_median, female_management_median],
    ["Marketing", male_marketing_median, female_marketing_median],
    ["Finance", male_finance_median, female_finance_median],
    ["Creative", male_creative_median, female_creative_median]
]
std_table = [
    ["Technology", male_technology_std, female_technology_std],
    ["Management", male_management_std, female_management_std],
    ["Marketing", male_marketing_std, female_marketing_std],
    ["Finance", male_finance_std, female_finance_std],
    ["Creative", male_creative_std, female_creative_std]
]
min_table = [
    ["Technology", male_technology_min, female_technology_min],
    ["Management", male_management_min, female_management_min],
    ["Marketing", male_marketing_min, female_marketing_min],
    ["Finance", male_finance_min, female_finance_min],
    ["Creative", male_creative_min, female_creative_min]
]
max_table = [
    ["Technology", male_technology_max, female_technology_max],
    ["Management", male_management_max, female_management_max],
    ["Marketing", male_marketing_max, female_marketing_max],
    ["Finance", male_finance_max, female_finance_max],
    ["Creative", male_creative_max, female_creative_max]
]
diff_table = [
    ["Technology", male_technology_diff, female_technology_diff],
    ["Management", male_management_diff, female_management_diff],
    ["Marketing", male_marketing_diff, female_marketing_diff],
    ["Finance", male_finance_diff, female_finance_diff],
    ["Creative", male_creative_diff, female_creative_diff]
]


#* Table creator function
def table_creator(table_data):
    formatted_table_data = []
    headers_list = ["Job Type", "Male", "Female"]

    for row in table_data:
        formatted_row = []
        for value in row:
            if isinstance(value, (int, float)):
                formatted_value = f"{round(value):,.0f}"  
            elif isinstance(value, str):
                formatted_value = value  
            else:
                formatted_value = str(value)  
            formatted_row.append(formatted_value)
        formatted_table_data.append(formatted_row)

    table = tabulate(formatted_table_data, headers_list, tablefmt="fancy_grid")
    return table

print("Mean Salary Table")
formatted_table = table_creator(mean_table)
print(formatted_table, '\n')

print("Median Salary Table")
formatted_table = table_creator(median_table)
print(formatted_table, '\n')

print("Standard Deviation Table")
formatted_table = table_creator(std_table)
print(formatted_table, '\n')

print("Maximum Salary Table")
formatted_table = table_creator(max_table)
print(formatted_table, '\n')

print("Minimum Salary Table")
formatted_table = table_creator(min_table)
print(formatted_table, '\n')

print("Salary Range Table")
formatted_table = table_creator(diff_table)
print(formatted_table, '\n')

#! race
#* Table data
mean_table = [
    ["White", male_white_mean, female_white_mean],
    ["Hispanic", male_Hispanic_mean, female_Hispanic_mean],
    ["Asian", male_Asian_mean, female_Asian_mean],
    ["Korean", male_Korean_mean, female_Korean_mean],
    ["Chinese", male_Chinese_mean, female_Chinese_mean],
    ["Australian", male_Australian_mean, female_Australian_mean],
    ["Welsh", male_Welsh_mean, female_Welsh_mean],
    ["African American", male_African_American_mean, female_African_American_mean],
    ["Mixed", male_Mixed_mean, female_Mixed_mean],
    ["Black", male_Black_mean, female_Black_mean]
]
median_table = [
    ["White", male_white_median, female_white_median],
    ["Hispanic", male_Hispanic_median, female_Hispanic_median],
    ["Asian", male_Asian_median, female_Asian_median],
    ["Korean", male_Korean_median, female_Korean_median],
    ["Chinese", male_Chinese_median, female_Chinese_median],
    ["Australian", male_Australian_median, female_Australian_median],
    ["Welsh", male_Welsh_median, female_Welsh_median],
    ["African American", male_African_American_median, female_African_American_median],
    ["Mixed", male_Mixed_median, female_Mixed_median],
    ["Black", male_Black_median, female_Black_median]
]
std_table = [
    ["White", male_white_std, female_white_std],
    ["Hispanic", male_Hispanic_std, female_Hispanic_std],
    ["Asian", male_Asian_std, female_Asian_std],
    ["Korean", male_Korean_std, female_Korean_std],
    ["Chinese", male_Chinese_std, female_Chinese_std],
    ["Australian", male_Australian_std, female_Australian_std],
    ["Welsh", male_Welsh_std, female_Welsh_std],
    ["African American", male_African_American_std, female_African_American_std],
    ["Mixed", male_Mixed_std, female_Mixed_std],
    ["Black", male_Black_std, female_Black_std]
]
min_table = [
    ["White", male_white_min, female_white_min],
    ["Hispanic", male_Hispanic_min, female_Hispanic_min],
    ["Asian", male_Asian_min, female_Asian_min],
    ["Koreana", male_Korean_min, female_Korean_min],
    ["Chinese", male_Chinese_min, female_Chinese_min],
    ["Australian", male_Australian_min, female_Australian_min],
    ["Welsh", male_Welsh_min, female_Welsh_min],
    ["African American", male_African_American_min, female_African_American_min],
    ["Mixed", male_Mixed_min, female_Mixed_min],
    ["Black", male_Black_min, female_Black_min]
]
max_table = [
    ["White", male_white_max, female_white_max],
    ["Hispanic", male_Hispanic_max, female_Hispanic_max],
    ["Asian", male_Asian_max, female_Asian_max],
    ["Korean", male_Korean_max, female_Korean_max],
    ["Chinese", male_Chinese_max, female_Chinese_max],
    ["Australian", male_Australian_max, female_Australian_max],
    ["Welsh", male_Welsh_max, female_Welsh_max],
    ["African American", male_African_American_max, female_African_American_max],
    ["Mixed", male_Mixed_max, female_Mixed_max],
    ["Black", male_Black_max, female_Black_max]
]
diff_table = [
    ["White", male_white_diff, female_white_diff],
    ["Hispanic", male_Hispanic_diff, female_Hispanic_diff],
    ["Asian", male_Asian_diff, female_Asian_diff],
    ["Korean", male_Korean_diff, female_Korean_diff],
    ["Chinese", male_Chinese_diff, female_Chinese_diff],
    ["Australian", male_Australian_diff, female_Australian_diff],
    ["Welsh", male_Welsh_diff, female_Welsh_diff],
    ["African American", male_African_American_diff, female_African_American_diff],
    ["Mixed", male_Mixed_diff, female_Mixed_diff],
    ["Black", male_Black_diff, female_Black_diff]
]


#* Table creator function
#? this function has been slightly modified to account for Nan values...
def table_creator(table_data):
    formatted_table_data = []

    for row in table_data:
        formatted_row = []
        headers_list = ["Race", "Male", "Female"]

        for value in row:
            if isinstance(value, (int, float)) and not math.isnan(value):
                formatted_value = f"{round(value):,.0f}"
            elif isinstance(value, str):
                formatted_value = value
            else:
                formatted_value = str(value)
            formatted_row.append(formatted_value)
        formatted_table_data.append(formatted_row)

    table = tabulate(formatted_table_data, headers_list, tablefmt="fancy_grid")
    return table

print("Mean Salary Table")
formatted_table = table_creator(mean_table)
print(formatted_table, '\n')

print("Median Salary Table")
formatted_table = table_creator(median_table)
print(formatted_table, '\n')

print("Standard Deviation Table")
formatted_table = table_creator(std_table)
print(formatted_table, '\n')

print("Maximum Salary Table")
formatted_table = table_creator(max_table)
print(formatted_table, '\n')

print("Minimum Salary Table")
formatted_table = table_creator(min_table)
print(formatted_table, '\n')

print("Salary Range Table")
formatted_table = table_creator(diff_table)
print(formatted_table, '\n')

#! years_experience
#* Table data
#? I could maybe write a function here do to do this for me but that would remove all my hard copy and pasting work :(
mean_table = [
    ["0-4 Years", male_0_4_years_mean, female_0_4_years_mean],
    ["5-10 Years", male_5_10_years_mean, female_5_10_years_mean],
    ["11-20 Years", male_11_20_years_mean, female_11_20_years_mean],
    ["20+ Years", male_20_plus_years_mean, female_20_plus_years_mean]
]
median_table = [
    ["0-4 Years", male_0_4_years_median, female_0_4_years_median],
    ["5-10 Years", male_5_10_years_median, female_5_10_years_median],
    ["11-20 Years", male_11_20_years_median, female_11_20_years_median],
    ["20+ Years", male_20_plus_years_median, female_20_plus_years_median]
]
std_table = [
    ["0-4 Years", male_0_4_years_std, female_0_4_years_std],
    ["5-10 Years", male_5_10_years_std, female_5_10_years_std],
    ["11-20 Years", male_11_20_years_std, female_11_20_years_std],
    ["20+ Years", male_20_plus_years_std, female_20_plus_years_std]
]
min_table = [
    ["0-4 Years", male_0_4_years_min, female_0_4_years_min],
    ["5-10 Years", male_5_10_years_min, female_5_10_years_min],
    ["11-20 Years", male_11_20_years_min, female_11_20_years_min],
    ["20+ Years", male_20_plus_years_min, female_20_plus_years_min]
]
max_table = [
    ["0-4 Years", male_0_4_years_max, female_0_4_years_max],
    ["5-10 Years", male_5_10_years_max, female_5_10_years_max],
    ["11-20 Years", male_11_20_years_max, female_11_20_years_max],
    ["20+ Years", male_20_plus_years_max, female_20_plus_years_max]
]
diff_table = [
    ["0-4 Years", male_0_4_years_diff, female_0_4_years_diff],
    ["5-10 Years", male_5_10_years_diff, female_5_10_years_diff],
    ["11-20 Years", male_11_20_years_diff, female_11_20_years_diff],
    ["20+ Years", male_20_plus_years_diff, female_20_plus_years_diff]
]


#* Table creator function
def table_creator(table_data):
    formatted_table_data = []
    headers_list = ["Years of Experience", "Male", "Female"]

    for row in table_data:
        formatted_row = []
        for value in row:
            if isinstance(value, (int, float)):
                formatted_value = f"{round(value):,.0f}"  
            elif isinstance(value, str):
                formatted_value = value  
            else:
                formatted_value = str(value)  
            formatted_row.append(formatted_value)
        formatted_table_data.append(formatted_row)

    table = tabulate(formatted_table_data, headers_list, tablefmt="fancy_grid")
    return table

print("Mean Salary Table")
formatted_table = table_creator(mean_table)
print(formatted_table, '\n')

print("Median Salary Table")
formatted_table = table_creator(median_table)
print(formatted_table, '\n')

print("Standard Deviation Table")
formatted_table = table_creator(std_table)
print(formatted_table, '\n')

print("Maximum Salary Table")
formatted_table = table_creator(max_table)
print(formatted_table, '\n')

print("Minimum Salary Table")
formatted_table = table_creator(min_table)
print(formatted_table, '\n')

print("Salary Range Table")
formatted_table = table_creator(diff_table)
print(formatted_table, '\n')
