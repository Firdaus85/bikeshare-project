import time
import pandas as pd
import numpy as np
import json

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }



MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']

DAYS = ['sunday', 'monday', 'tuesday', 'wednesday', \
        'thursday', 'friday', 'saturday' ]

def get_inputs():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                 '\nWould you like to see data for Chicago , New York city , or Washington ?\n')
        if city in CITY_DATA:
            break
            
    city=city.lower()
    
       
    
    
    
    

  

   
    


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('All right! please it\'s time to provide us a month name''or just say \'all\' to apply no month filter. \n(e.g.all january, feburary, march, april, may, june) \n> '.format(MONTHS))
        if month in MONTHS:
            break
    month=month.lower()
     
   
   
    
     


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('One Last thing. Could you type one of the week day you want to analyse?''You can type \'all\' again to apply no day filter. \n(e.g. all, monday, ....., sunday) \n>'.format(DAYS))
        if day in DAYS:
            break
            
    day=day.lower()
        
        
   
 
    
    
            
            
    
    
        
    
    


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
    df = pd.read_csv(CITY_DATA[city])
    #add datetime format to permit easy filtering
    df['Start Time'] = pd.to_datetime(df['Start Time'])


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['month'] = df['Start Time'].dt.month
    df['hour'] = df["Start Time"].dt.hour

    # TO DO: display the most common month
    common_month=df['month'].mode()[0]
    print('Most common month:',common_month)


    # TO DO: display the most common day of week
    common_day_of_week=df['day_of_week'].mode()[0]
    print('Most common day of week:',common_day_of_week)


    # TO DO: display the most common start hour
    common_start_hour=df['hour'].mode()[0]
    print('Most common hour:',common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    commonly_used_start_station=df['Start Station'].mode()[0]
    print("The most commonly used start station:", commonly_used_start_station)


    # TO DO: display most commonly used end station
    commonly_used_end_station=df['End Station'].mode()[0]
    print("The most commonly used end station:", commonly_used_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    df['Start End']=df['Start Station'].map(str)+'&'+df['End Station']
    popular_start_end=df['Start End'].value_counts().idxmax()
    print('The most frequent combination of start station and end station:',popular_start_end)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time :", total_travel_time)


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time :", mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Counts of user types:\n")
    user_counts = df['User Type'].value_counts()
    # iteratively print out the total numbers of user types 
    for index, user_count in enumerate(user_counts):
        print("  {}: {}".format(user_counts.index[index], user_count))

    print()

    
     
     


    # TO DO: Display counts of gender
    try:
        print('\n* What is the breakdown of gender among users?\n')

        return df['Gender'].value_counts()
        
    except:
        print('There is no gender data in the source.')
   
   
   
    


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print('\n* What is the earliest, latest, and most frequent year of birth, respectively?')
        earliest = np.min(df['Birth Year'])
        print ("\nThe earliest year of birth is " + str(earliest) + "\n")
        latest = np.max(df['Birth Year'])
        print ("The latest year of birth is " + str(latest) + "\n")
        most_frequent= df['Birth Year'].mode()[0]
        print ("The most frequent year of birth is " + str(most_frequent) + "\n")
        return earliest, latest, most_frequent
    except:
        print('No available birth date data for this period.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    

            
def display_data(df):
    """Displays raw bikeshare data."""
    row_length = df.shape[0]

    # iterate from 0 to the number of rows in steps of 5
    for i in range(0, row_length, 5):

        yes = input('\nWould you like to examine the particular user trip data? Type \'yes\' or \'no\'\n> ')
        if yes.lower() != 'yes':
            break

        # retrieve and convert data to json format
        # split each json row data 
        row_data = df.iloc[i: i + 5].to_json(orient='records', lines=True).split('\n')
        for row in row_data:
            # pretty print each user data
            parsed_row = json.loads(row)
            json_row = json.dumps(parsed_row, indent=2)
            print(json_row)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
