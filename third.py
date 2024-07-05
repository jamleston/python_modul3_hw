import re

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

def normalize_phone(phone_number):
    pattern = r'\D'
    list_of_num = re.split(pattern, phone_number)
    num = ''
    for el in list_of_num:
        num+= el
    if num.startswith('38'):
        num = '+' + num
    else:
        num = '+38' + num
    return num

# return one phone number
result = normalize_phone(raw_numbers[0])
print(result)

# return full list of phone numbers
sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)