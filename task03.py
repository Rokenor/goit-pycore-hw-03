import re

def normalize_phone(phone_number: str):
  list_of_matched_symbols = re.findall(r"\+|\d+", phone_number)

  normalized_string = "".join(list_of_matched_symbols)

  match normalized_string[:1]:
    case "0":
        return f'+38{normalized_string}'
    case "3":
        return f'+{normalized_string}'
    case _:
        return normalized_string


#example
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)