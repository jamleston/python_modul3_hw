from datetime import datetime

# user_input = input('please give num:')

def get_days_from_today(date_string):
        new_date = datetime.strptime(date_string,"%Y-%m-%d")
        new_date = new_date.date()
        today_date = datetime.today().date()
        # print(new_date)
        # print(today_date)
        timedelta = new_date - today_date
        return timedelta.days
    # except ValueError:
    #         print("Oops!  That was no valid number.  Try again with this format 'year-month-day'")
    #         user_date = input('--->')
    #         result = get_days_from_today(user_date)
    #         return result

# user_input = input('please give num:')
result = get_days_from_today('2020-10-09')
print(result)
# '2020-11-09'