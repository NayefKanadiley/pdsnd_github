import time
import pandas as pd
import numpy as np

CITY_DATA = {'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv'}

def check_input(input_str,input_type):


    while True:
        input_read=input(input_str)
        try:
            if input_read in ['Chicago','New York City','Washington'] and input_type == 0:
                break
            elif input_read in ['all', 'jan', 'feb', 'mar', 'apr', 'may', 'jun'] and input_type == 1:
                break
            elif input_read in ['all','sunday','monday','tuesday','wednesday','thursday','friday','saturday'] and input_type == 2:
                break
            else:
                if input_type == 0:
                    print("Oops! :(\n write only one of these three cities: Chicago, New York City or Washington \n Hint: Don\'t forget the capital letter!")
                if input_type == 1:
                    print("Oops! :(\n write the correct shortcut from: jan, feb, mar, apr, may, or jun. OR all if you want all of them!")
                if input_type == 2:
                    print("Oops! :(\n write the correct day from: sunday, monday, tuesday, wednesday, thursday, friday, saturday, OR input all if you want all of them!")
        except ValueError:
            print("Oops! :( check your input please")
    return input_read

def get_filters():


    print('Hello! :)\n My name is Python! xD\n Let\'s explore some US bikeshare data!\n')

    city = check_input("\n Firstly, \n tell me which city do you want? :) \n Chicago, New York City or Washington?\n\n",0)

    month = check_input("\n SURE!\n Now, Which Month? Please write the appropriate shortcut from:\n (jan, feb, mar, apr, may, jun, OR all)\n\n", 1)

    day = check_input("\n OK!\n Now, Which day? Please write the appropriate shortcut from: (sunday, monday, tuesday, wednesday, thursday, friday, saturday OR all)\n\n", 2)
    print('-'*40)
    return city, month, day

def load_data(city, month, day):


    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':

        months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun']
        month = months.index(month) + 1

        df = df[df['month'] == month]


    if day != 'all':

        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):


    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    common_month = df['month'].mode()[0]
    print('The Most common Month:', common_month)

    common_day_of_week = df['day_of_week'].mode()[0]
    print('The Most Day Of Week:', common_day_of_week)

    common_start_hour = df['hour'].mode()[0]
    print('The Most Common Start Hour:', common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    common_start_station = df['Start Station'].mode()[0]
    print('The Most Start Station:', common_start_station)

    common_end_station = df['End Station'].mode()[0]
    print('The Most End Station:', common_end_station)

    group_field=df.groupby(['Start Station','End Station'])

    common_station = group_field.size().sort_values(ascending=False).head(1)
    print('The Most frequent combination of Start Station and End Station trip:\n', common_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time:', total_travel_time)

    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    print('The counts of User Type Stats:')
    print(df['User Type'].value_counts())


    if city.lower() != 'washington':

        print('Gender Stats:')
        print(df['Gender'].value_counts())

        print('Birth Year Stats:')

        most_common_year = df['Birth Year'].mode()[0]
        print('The Most Common Year:',most_common_year)

        most_recent_year = df['Birth Year'].max()
        print('The Most Recent Year:',most_recent_year)

        earliest_year = df['Birth Year'].min()
        print('The Earliest Year:',earliest_year)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    keep_asking = True
    while (keep_asking):
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        view_display = input("Do you wish to continue?: ").lower()
        if view_display == "no":
            keep_asking = False
                   

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nNeed more information? :)\n Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
