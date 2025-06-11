from datetime import datetime

def get_days_from_today(date):
  try:
    input_date_list = []

    for key in date.split("-"):
      input_date_list.append(int(key))

    input_date = datetime(input_date_list[0], input_date_list[1], input_date_list[2])
    today = datetime.now()
    days_different = today.toordinal() - input_date.toordinal()

    return days_different
  except:
    print(f'Input string is not a date in format YYYY-MM-DD\nYour input date is: {date}')
    return 0

#self-checks
print(get_days_from_today("2020-10-09"))
print(get_days_from_today("2026-10-09"))
print(get_days_from_today(123))
print(get_days_from_today('asdasd'))