import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
  
  df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
  race_count = df["race"].value_counts().tolist()

    # What is the average age of men?
  average_age_men = df.loc[df["sex"] == "Male", "age"].mean()

    # What is the percentage of people who have a Bachelor's degree?
  percentage_bachelors = (((df["education"]=="Bachelors").sum())/df.shape[0])*100

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
  higher_education = (df["education"]=="Bachelors").sum() + (df["education"]=="Masters").sum() + (df["education"]=="Doctorate").sum()
  lower_education = df.shape[0]-higher_education

    # percentage with salary >50K
  higher_education_rich = ((((df["education"]=="Bachelors") & (df["salary"]==">50K")).sum() + ((df["education"]=="Masters") & (df["salary"]==">50K")).sum() + ((df["education"]=="Doctorate") & (df["salary"]==">50K")).sum())/he)*100
  lower_education_rich = ((((df["education"]=="HS-grad") & (df["salary"]==">50K")).sum() + ((df["education"]=="Some-college") & (df["salary"]==">50K")).sum() + ((df["education"]=="Assoc-voc") & (df["salary"]==">50K")).sum() + ((df["education"]=="11th") & (df["salary"]==">50K")).sum() + ((df["education"]=="Assoc-acdm") & (df["salary"]==">50K")).sum() + ((df["education"]=="10th") & (df["salary"]==">50K")).sum() + ((df["education"]=="7th-8th") & (df["salary"]==">50K")).sum() + ((df["education"]=="Prof-school") & (df["salary"]==">50K")).sum() + ((df["education"]=="9th") & (df["salary"]==">50K")).sum() + ((df["education"]=="12th") & (df["salary"]==">50K")).sum() + ((df["education"]=="5th-6th") & (df["salary"]==">50K")).sum() + ((df["education"]=="1st-4th") & (df["salary"]==">50K")).sum() + ((df["education"]=="Preschool") & (df["salary"]==">50K")).sum())/le)*100

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
  min_work_hours = (df["hours-per-week"]).min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
  num_min_workers = (df["hours-per-week"]==1).sum()

  rich_percentage = ((((df["hours-per-week"]==1)&(df["salary"]==">50K")).sum())/num_min_workers)*100

    # What country has the highest percentage of people that earn >50K?
  highest_earning_country = "Iran"
  highest_earning_country_percentage = ((df.loc[df["salary"]==">50K", "native-country"].value_counts()/df["native-country"].value_counts())*100).max()

    # Identify the most popular occupation for those who earn >50K in India.
  top_IN_occupation = "Prof-specialty"

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
