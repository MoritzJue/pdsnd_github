import time
import pandas as pd
import numpy as np

# create dataframe
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# set up functions
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('\nHello! Let\'s explore some US bikeshare data!')

    while True:
      city = input("\nPlease indicate for which city would you like to filter by? Chicago, New York City, or Washington?\n").lower()
      if city not in ('new york city', 'chicago', 'washington'):
        print("It seems like you did not choose one of the stated cities. Please try again.")
        continue
      else:
        break

    while True:
      month = input("\nPlease indicate for which month would you like to filter by? January, February, March, April, May, June or type 'all' if you do not have any preference?\n")
      if month not in ('January', 'February', 'March', 'April', 'May', 'June', 'all'):
        print("It seems like you did not choose one of the stated options. Please try again.")
        continue
      else:
        break

    while True:
      day = input("\nPlease indicate for what particular day you are looking? Please enter the day as follows: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday. Enter 'all' if you do not have any preference.\n")
      if day not in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'all'):
        print("It seems like you did not choose one of the stated options. Please try again.")
        continue
      else:
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
   	 	# use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

    	# filter by month to create the new dataframe
        df = df[df['month'] == month]

        # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most favoured month
    favoured_month = df['month'].mode()[0]
    print('Most Favoured Month:', favoured_month)

    # display the most favoured week
    favoured_day = df['day_of_week'].mode()[0]
    print('Most Favoured day:', favoured_day)

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
        
    # display the most favoured hour
    favoured_hour = df['hour'].mode()[0]
    print('Most Common Hour:', favoured_hour)

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most favoured start station
    Start_Station = df['Start Station'].value_counts().idxmax()
    print('The most commonly used start station is:', Start_Station)

    # display most favoured end station
    End_Station = df['End Station'].value_counts().idxmax()
    print('\nThe most commonly used end station is:', End_Station)

    # display most favoured combination station
    Combination_Station = df.groupby(['Start Station', 'End Station']).count()
    print('\nThe most commonly used combination of start station and end station trip is:', Start_Station, " & ", End_Station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display sum travel time
    Total_Travel_Time = sum(df['Trip Duration'])
    print('\nTotal travel time is {} days'.format(Total_Travel_Time/86400))
    
    # display mean travel time
    Mean_Travel_Time = df['Trip Duration'].mean()
    print('\nMean travel time is {} minutes'.format(Mean_Travel_Time/60))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # print value counts for each user type
    user_types = df['User Type'].value_counts()
    #print(user_types)
    print('\nThe value count for each user type is:\n{}\n'.format(user_types))
    
    # print counts of gender
    try:
      gender_types = df['gender'].value_counts()
      print('\nGender Types:\n', gender)
      print('\nThe value count for each gender is:\n{}\n'.format(gender))
    except KeyError:
      print("\nGender Types:\nNo data available for this time period.")

     # display minimum, maximum, and most frequent year of birth
    try:
      Min_Year = df['Birth Year'].min()
      print('\nThe minimum birth year is:\n{}\n'.format(Min_Year))
    except KeyError:
      print("\nMin Year:\nNo data available for this time period.")

    try:
      Max_Year = df['Birth Year'].max()
      print('\nThe maximum birth year is:\n{}\n'.format(Max_Year))
    except KeyError:
      print("\nMax Year:\nNo data available for this time period.")

    try:
      Most_Frequent_Year = df['birth year'].value_counts().idxmax()
      print('\nMost Common Year:', Most_Common_Year)
      print('\nThe most frequent birth year is:\n{}\n'.format(Most_Frequent_Year))
    except KeyError:
      print("\nMost Frequent Year:\nNo data available for this time period.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    
def raw_data(df):
    user_input = input('Do you want to see raw data? Enter yes or no.\n')
    line_number = 0

    while 1 == 1 :
        if user_input.lower() != 'no':
            print(df.iloc[line_number : line_number + 5])
            line_number += 5
            user_input = input('\nDo you want to see more raw data? Enter yes or no.\n')
        else:
            break    

         
            
            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()