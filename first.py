from datetime import datetime

def get_days_from_today(date_string):
    try:
        new_date = datetime.strptime(date_string,"%Y-%m-%d")
        new_date = new_date.date()
        today_date = datetime.today().date()
        # print(new_date)
        # print(today_date)
        timedelta = new_date - today_date
        return timedelta.days
    except ValueError:
            print("Oops!  That was no valid number.  Try again with this format 'year-month-day'")
            user_date = input('please give right num: ')
            result = get_days_from_today(user_date)
            return result

user_input = input('please give num: ')
result = get_days_from_today(user_input)
print(result)
# '2020-11-09'