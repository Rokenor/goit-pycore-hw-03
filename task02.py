import random

def get_numbers_ticket(min, max, quantity):
  if min < 1:
    return 'min can\'t be less than 1'
  if max > 1000:
    return 'max can\'t be more than 1000'
  if quantity <=0:
    quantity = 1

  numbers_list = set()
  
  while len(numbers_list) < quantity:
    random_number = random.randint(min, max)
    numbers_list.add(random_number)

  result_list = list(numbers_list)
  result_list.sort()

  return result_list

#self-checks
print(get_numbers_ticket(1, 10, 5));
print(get_numbers_ticket(100, 200, 10));
print(get_numbers_ticket(10, 200, 0));

#example
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)