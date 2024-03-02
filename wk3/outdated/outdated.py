months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:

    # Get date from user

    date = input('Date: ')

    # Split date into month, day, and year variables if in mm/dd/yyyy format

    try: 
        month, day, year = date.split('/')
        if (int(month) >= 1 and int(month) <= 12) and (int(day) >= 1 and int(day) <= 31):
            break
    except:

        # Split date into month, day, and year variables if in Month Day, Year format, as well as remove the comma separator

        try: 
            new_month, new_day, year = date.split(' ')
            for i in range(len(months)):
                if new_month == months[i]:
                    month = i + 1
            day = new_day.replace(',', '')
            if (int(month) >= 1 and int(month) <= 12) and (int(day) >= 1 and int(day) <= 31):
                break
        except:
            print()
            pass

# Arrange the date in yyyy-mm-dd format and print to console

print(f'{int(year)}-{int(month)}-{int(day)}')

