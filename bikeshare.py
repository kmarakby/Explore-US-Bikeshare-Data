import time
import datetime
import calendar
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
       # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        #cities= ['all','chicago','new york city','washington']
        city= input("\n Choose a City? (Chicago, New york city, Washington) \n").lower()
        if city in CITY_DATA:
            break
        else:
            print("\n Not a valid city")    
        
    # get user input for month (all, january, february, ... , june)
    while True:
        months= ['All','January','February','March','April','May','June']
        month= input("\n Choose a Month? (January , February , March , April , May ,June or All) \n").title()
        if month in months:
            break
        else:
            print("\n Not a valid Month")
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        days= ['All','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        day= input("\n Choose a Day? (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday , All) \n").title()
        if day in days:
            break
        else:
            print("\n Not a valid Day")
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

# load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'All':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def display_raw_data(df):
    """ Ask user if he wants to display the first 5 raws of raw data """
    i = 0
    raw = input('\nDisplay the first 5 raws of data? Enter yes or no \n').lower() # TO DO: convert the user input to lower case using lower() function
    pd.set_option('display.max_columns',None)

    while True:            
        if raw == 'no':
            break
        elif raw == 'yes':
            print(df[i:i+5]) # TO DO: appropriately subset/slice your dataframe to display next five rows
            raw = input('\nDisplay the next 5 raws of data? Enter yes or no \n').lower() # TO DO: convert the user input to lower case using lower() function
            i += 5
        else:
            raw = input('\nYour input is invalid. Please enter only yes or no \n').lower()
            
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    cm = calendar.month_name[common_month]
    print("The Most Common Month :" ,cm)

    # TO DO: display the most common day of week
    day_of_week = df['day_of_week'].mode()[0]
    print("The Most Common Day :" ,day_of_week)

    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    csh = df['hour'].mode()[0]
    print('Most common Start Hour :', csh)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    mcuss = df['Start Station'].mode()[0]
    print("The Most Commonly Used Start Station :" ,mcuss)


    # TO DO: display most commonly used end station
    mcues = df['End Station'].mode()[0]
    print("The Most Commonly Used End Station :" ,mcues)

    # TO DO: display most frequent combination of start station and end station trip
    combo = ('From '+df['Start Station']+' To '+df['End Station']).mode()[0]
    print("The Most Frequent Station Combination :" ,combo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    ttt=df['Trip Duration'].sum()
    print("Total Travel Time in Seconds :" ,ttt)
    # TO DO: display mean travel time
    mtt=int(round(df['Trip Duration'].mean()))
    print("Mean Travel Time in Seconds :" ,mtt)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('counts of user types:' ,user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        Gender  = df['Gender'].value_counts()
        print('counts of Gender:' ,Gender)
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        mcy= int(df['Birth Year'].mode()[0])
        mey= int(df['Birth Year'].min())
        mry= int(df['Birth Year'].max())
        
        print('Most Common Year of Birth :',mcy)
        print('Most Earliest Year of Birth :',mey)
        print('Most Recent Year of Birth :',mry)
    
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
