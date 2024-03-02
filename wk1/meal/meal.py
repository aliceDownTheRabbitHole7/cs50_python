def main():

    # Get current time from user

    curr_time = input('Current time: ')

    # Convert time to a decimal

    time_int = convert(curr_time)

    # Check to see if it is meal time at the current moment

    if 7 <= time_int <= 8:
        print('breakfast time')
    elif 12 <= time_int <= 13:
        print('lunch time')
    elif 18 <= time_int <= 19:
        print('dinner time')
    else:
        pass

def convert(time):

    # Split the string to get the hour and minutes

    time_split = time.split(':')

    # Split again to find minutes whether it is in military time or in 12 hour standard

    new_split = time_split[1].split(' ')

    # Store the hour and minutes

    hour = int(time_split[0])
    minute = int(new_split[0])

    # Calculations if the input is in 12 hour standard
    
    if 'pm' in time or 'p.m'in time or 'PM' in time or 'P.M.' in time:
        if '12' in time:
            pass
        else:
            hour += 12
    else:
        pass

    # convert the time into a floating integer
    
    min_float = minute/60
    converted_time = hour + min_float
    return converted_time

if __name__ == '__main__':
    main()