import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Would you like to see data for Chicago, New York, or Washington?').lower()
        if city not in CITY_DATA:
            print('That is not one of the available cities.')
            continue

        # TO DO: get user input for month (all, january, february, ... , june)
        month = input('Which month would you like to view data for (or all)?').lower()
        if month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            print('That is not a valid month.')
            continue

        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        day = input('Which day of the week would you like to view data for (or all)?').lower()
        if day not in ['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']:
            print('That is not a valid day of the week.')
            continue
        
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
    #use CITY_DATA dictionary to read from correct file
    olddf = pd.read_csv(CITY_DATA[city])
    
    #create new columns for month, day, and hour
    olddf['Start Time'] = pd.to_datetime(olddf['Start Time'])
    olddf['month'] = olddf['Start Time'].dt.month_name()
    #print(df['month'])
    olddf['dayofweek'] = olddf['Start Time'].dt.day_name()
    
    olddf['startHour'] = olddf['Start Time'].dt.hour
    #print(df['dayofweek'])
    

    #filter data for correct month and day based on new columns
    #make exception for all months and days
    if month == 'all' and day == 'all':
        df = olddf
    elif month == 'all':
         df = olddf[(olddf['dayofweek'] == day.title())]
    elif day == 'all':
         df = olddf[(olddf['month'] == month.title())]
    else:
         df = olddf[(olddf['month'] == month.title())&(olddf['dayofweek'] == day.title())]
    
    return df, olddf


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    monthMode = df['month'].mode().item()
    print('The most common month is', monthMode)

    # TO DO: display the most common day of week
    dayMode = df['dayofweek'].mode().item()
    print('The most common day of week is', dayMode)

    # TO DO: display the most common start hour
    hourMode = df['startHour'].mode().item()
    print('The  most common start hour is', hourMode)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    startMode = df['Start Station'].mode().item()
    print('The most common start station is', startMode)

    # TO DO: display most commonly used end station
    endMode = df['End Station'].mode().item()
    print('The most common end station is', endMode)

    # TO DO: display most frequent combination of start station and end station trip
    df['route'] = df['Start Station'] + ' to ' + df['End Station']
    routeMode = df['route'].mode().item()
    print('The most common route is', routeMode)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    totalTime = df['Trip Duration'].sum().item()
    print('The total travel time is', totalTime)

    # TO DO: display mean travel time
    meanTime = df['Trip Duration'].mean().item()
    print('The mean travel time is', meanTime)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    userTypes = df['User Type'].value_counts()
    print('The user type counts are \n', userTypes)

    # TO DO: Display counts of gender
    if city != 'washington':
        gender = df['Gender'].value_counts()
        print('The gender counts are \n', gender)

        # TO DO: Display earliest, most recent, and most common year of birth
        minYear = df['Birth Year'].min()
        print('The earliest birth year is', minYear.astype(int))
    
        maxYear = df['Birth Year'].max()
        print('The most recent birth year is', maxYear.astype(int))
    
        modeYear = df['Birth Year'].mode().item()
        print('The most common birth year is', modeYear)
    
    else: print('Washington does not collect gender or birth year data.')
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):
  
    i = 0
    print(df.loc[i])
    print(df.loc[i + 1])
    print(df.loc[i + 2])
    print(df.loc[i + 3])
    print(df.loc[i + 4])
    i += 4
    
    while True:
        cont = input('Would you like to see more raw data?\n').lower()
        if cont == 'yes':
            print(df.loc[i])
            print(df.loc[i + 1])
            print(df.loc[i + 2])
            print(df.loc[i + 3])
            print(df.loc[i + 4])
            i += 4
        elif cont == 'no':
            break
        else:
            print('Please choose yes or no.')
            continue
    
    
def main():
    while True:
        city, month, day = get_filters()
        df, olddf = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        raw_data(olddf)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

	print('Thank you for using my program!')
if __name__ == "__main__":
	main()

