import pandas as pd
import numpy as np


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")
    print(df)

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df["race"].value_counts().squeeze()

    # What is the average age of men?
    male = df[df["sex"] == "Male"]
    average_age_men = round(male.age.mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    education = df["education"].value_counts(normalize = True)*100
    percentage_bachelors = education["Bachelors"].round(1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
   

    

    # percentage with salary >50K
    mask_edu = df["education"].isin(["Masters","Bachelors", "Doctorate"])
    higher_ed = df[mask_edu]
    mask_salary = higher_ed["salary"] == ">50K" 

    higher_education_rich = np.round(higher_ed[mask_salary].shape[0]/higher_ed.shape[0]*100, 1)
    lower_ed = df[mask_edu == False]
    mask_salary_low = lower_ed["salary"] == ">50K"
    lower_education_rich = np.round((lower_ed[mask_salary_low].shape[0]/df[mask_edu == False].shape[0]*100),1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?

    mask_hours = df["hours-per-week"] == 1  

    min_hours = df[mask_hours] 

    rich_mask = min_hours["salary"] == ">50K"

    min_hours[rich_mask].shape[0]
    num_min_workers = df[mask_hours].shape[0]
    

    rich_percentage = (min_hours[rich_mask].shape[0]/num_min_workers)*100

    # What country has the highest percentage of people that earn >50K?

    richdf = df.groupby(["native-country", "salary"]).size().unstack()

    richdf["total"] = richdf["<=50K"] + richdf[">50K"]
    richdf["rich_percentage"] = round(richdf[">50K"]/richdf["total"]*100, 1)
    richdf


    
    highest_earning_country = richdf["rich_percentage"].idxmax()
    highest_earning_country_percentage = richdf["rich_percentage"].max()

    # Identify the most popular occupation for those who earn >50K in India.
    rich_indians = df[(df["native-country"]=="India") & (df["salary"] == ">50K")]

    top_IN_occupation = rich_indians["occupation"].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
