from datetime import datetime, timedelta

def get_days_from_today(date_string):
    new_date = datetime.strptime(date_string,"%Y-%m-%d")
    new_date = new_date.date()
    today_date = datetime.today().date()
    # print(new_date)
    # print(today_date)
    timedelta = new_date - today_date
    return timedelta.days

result = get_days_from_today('2020-10-09')
print(result)
