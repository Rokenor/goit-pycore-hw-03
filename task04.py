'''
У межах вашої організації, ви відповідаєте за організацію привітань колег з днем народження. 
Щоб оптимізувати цей процес, вам потрібно створити функцію get_upcoming_birthdays, 
яка допоможе вам визначати, кого з колег потрібно привітати. Функція повинна повернути 
список всіх у кого день народження вперед на 7 днів включаючи поточний день.

У вашому розпорядженні є список users, кожен елемент якого містить інформацію про ім'я 
користувача та його день народження. Оскільки дні народження колег можуть припадати на вихідні, 
ваша функція також повинна враховувати це та переносити дату привітання на наступний робочий день, 
якщо необхідно.
'''

'''
Параметр функції users - це список словників, де кожен словник містить ключі name (ім'я користувача, рядок) та birthday (день народження, рядок у форматі 'рік.місяць.дата').
Функція має визначати, чиї дні народження випадають вперед на 7 днів включаючи поточний день. Якщо день народження припадає на вихідний, дата привітання переноситься на наступний понеділок.
Функція повертає список словників, де кожен словник містить інформацію про користувача (ключ name) та дату привітання (ключ congratulation_date, дані якого у форматі рядка 'рік.місяць.дата').
'''
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