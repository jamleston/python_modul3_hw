import random

def get_numbers_ticket(min, max, quantity):
    final_list = []
    if min>=1 and max>=1 and max<=1000 and quantity<=max-min+1:

        counter = 0
        while counter < quantity:
            random_num = random.randrange(min, max+1)
            if random_num in final_list:
                pass
            else:
                final_list.append(random_num)
                counter+=1
    else:
        print(final_list)
    final_list.sort()
    print(final_list)
    return final_list

input_min = int(input('min: '))
input_max = int(input('max: '))
input_quantity = int(input('quantity: '))


get_numbers_ticket(input_min, input_max, input_quantity)