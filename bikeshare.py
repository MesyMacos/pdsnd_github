import time
import pandas as pd
import numpy as np

# A dictionary to hold the csv files
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities = ['chicago', 'new york', 'washington']

months = [ "january", "february", "march", "april", "may", "june", "all" ]

days   = [ "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all" ]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Select the city you would like to filter by: Chicago, New York or Washington? \n> ').lower()
        if city in cities:
            break
                
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Select the month you would like to filter by: \n (January, February, March, April, May, June)\n Or select "all" for no filter.\n>').lower()
        if month in months:
            break
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Select the day you would like to filter by: \n (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday)\n Or select "all" for no filter.\n>').lower()
        if day in days:
            break
            
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #reading in the data set
    df = pd.read_csv(CITY_DATA[city], index_col = 0)
    
    
    #Creating columns
    df['Start Time'] = pd.to_datetime(df['Start Time'])     
    df["month"] = df['Start Time'].dt.month                 
    df["week_day"] = df['Start Time'].dt.weekday_name       
    df["start_hour"] = df['Start Time'].dt.hour              
    df["start_end"] = df['Start Station'].astype(str) + ' to ' + df['End Station']

    if month != 'all':
        month_index = months.index(month) + 1      
        df = df[df["month"] == month_index ]                

    if day != 'all':
        df = df[df["week_day"] == day.title() ]             

    return df
    
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    month_index = df["month"].mode()[0] - 1
    most_common_month = months[month_index].title()
    print("Most common month: ", most_common_month)

    # TO DO: display the most common day of week
    most_common_dayofweek = df["week_day"].mode()[0]
    print("Most common day of week: ", most_common_dayofweek)

    # TO DO: display the most common start hour
    most_common_start_hour = df["start_hour"].mode()[0]
    print("Most common start hour: ", most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_used_start_station = df['Start Station'].mode()[0]
    print("Most commonly used start station: ", most_used_start_station)

    # TO DO: display most commonly used end station
    most_used_end_station = df['End Station'].mode()[0]
    print("Most commony used end station: ", most_used_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_combination = df["start_end"].mode()[0]
    print("Most frequent combination of start and end station trip: ", most_frequent_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print("Total travel time: ", str(round(total_travel_time/3600, 2)), "hours or", str(round(total_travel_time/60, 2)), "minutes or", total_travel_time, "seconds")   
    
    # TO DO: display mean travel time
    mean_time = df["Trip Duration"].mean()
    print("The mean travel time: ", str(round(mean_time/3600, 2)), "hours or", str(round(mean_time/60, 2)), "minutes or", str(round(mean_time, 2)), "seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Counts of user types: ", df["User Type"].value_counts())

    # TO DO: Display counts of gender
    if "Gender" in df:
        print("\nCounts concerning gender of clients")
        print("Women: ", df.query("Gender == 'Female'").Gender.count())
        print("Men: ", df.query("Gender == 'Male'").Gender.count())
       

    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df:
        print("\nEarliest year of birth: ", df["Birth Year"].min())
        print("Most recent year of birth: ", df["Birth Year"].max())
        print("Most common year of birth: ", df["Birth Year"].value_counts().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """Displays raw data on bikeshare users."""
    
    print('\nDisplaying raw data on bikeshare users ...\n')
    start_time = time.time()
   
    display = input('Would you like to see the first five rows of the raw data? YES or NO?\n')
    line_number = 0
    """ If this condition is True; show the user the next 5 lines of records"""
    while True :
        if display.lower() != 'no':
            print(df.iloc[line_number : line_number + 5])
            line_number += 5
            display = input('Would you like to see the next five rows of the raw data? YES or NO?\n')
        else:
            break
            
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()