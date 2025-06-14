from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    result = []

    today = datetime.today().date()

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        birthday_difference = (birthday_this_year - today).days

        if birthday_difference >= 0 and birthday_difference <= 7:
            birthday_day_of_week = birthday_this_year.weekday()

            if birthday_day_of_week == 5:
                birthday_this_year = birthday_this_year + timedelta(days=2)
            elif birthday_day_of_week == 6:
                birthday_this_year = birthday_this_year + timedelta(days=1)
        
            
            if (birthday_this_year - today).days <=7:
                user_with_birthday_next_week = {"name": user["name"], "congratulation_date": str(birthday_this_year)}
                
                result.append(user_with_birthday_next_week)

    return result

# example
users = [
    {"name": "John Smith", "birthday": "1990.01.14"},
    {"name": "Emily Jones", "birthday": "1985.06.17"},
    {"name": "Michael Williams", "birthday": "1990.06.18"},
    {"name": "Sarah Brown", "birthday": "1994.08.19"},
    {"name": "David Davis", "birthday": "1999.06.20"},
    {"name": "Jessica Miller", "birthday": "1982.06.21"},
    {"name": "James Wilson", "birthday": "1990.06.22"},
    {"name": "Jennifer Moore", "birthday": "2000.01.10"},
    {"name": "Robert Taylor", "birthday": "1993.06.14"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)