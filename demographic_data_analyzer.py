import pandas as pd
import numpy as np

def calculate_demographic_data(print_data=True):
    data = pd.read_csv('adult.data.csv')
    race_count = data['race'].value_counts()
    average_age_men = round(data[data['sex'] == 'Male']['age'].mean(), 1)




    percentage_bachelors = round(100 * data['education'].value_counts(normalize=True)['Bachelors'], 1)
    higher_education = data[data['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = data[~data['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    
    # Calculate the percentage of high earners (>50K) among those with higher education
    higher_education_rich = round(100 * (higher_education['salary'] == '>50K').mean(), 1)
    
    # Calculate the percentage of high earners (>50K) among those without higher education
    lower_education_rich = round(100 * (lower_education['salary'] == '>50K').mean(), 1)
    
    # Identify the minimum weekly work hours in the dataset
    min_work_hours = data['hours-per-week'].min()
    
    # Isolate individuals working the minimum number of hours per week
    num_min_workers = data[data['hours-per-week'] == min_work_hours]
    
    # Compute the percentage of high earners among those working minimum hours
    rich_percentage = round(100 * (num_min_workers['salary'] == '>50K').mean(), 1)
    
    # Analyze the proportion of high earners by country of origin
    country_stats = data.groupby('native-country')['salary'].apply(lambda x: (x == '>50K').mean()).sort_values(ascending=False)
    
    # Identify the country with the highest percentage of high earners
    highest_earning_country = country_stats.index[0]
    
    # Determine the highest percentage of high earners in any country
    highest_earning_country_percentage = round(100 * country_stats.iloc[0], 1)
    
    # Find the most prevalent occupation among high-earning individuals from India
    top_IN_occupation = data[(data['native-country'] == 'India') & (data['salary'] == '>50K')]['occupation'].value_counts().index[0]

    # Display the results if print_data is True
    if print_data:
        print("Racial distribution in the dataset:\n", race_count)
        print("\nAverage age of male participants:", average_age_men)
        print(f"\nPercentage of individuals with a Bachelor's degree: {percentage_bachelors}%")
        print(f"\nPercentage of high earners with higher education: {higher_education_rich}%")
        print(f"Percentage of high earners without higher education: {lower_education_rich}%")
        print(f"\nMinimum weekly work hours: {min_work_hours} hours/week")
        print(f"Percentage of high earners among minimum hour workers: {rich_percentage}%")
        print(f"\nCountry with the highest percentage of high earners: {highest_earning_country}")
        print(f"Highest percentage of high earners by country: {highest_earning_country_percentage}%")
        print(f"\nMost common occupation among high-earning Indians: {top_IN_occupation}")





 







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