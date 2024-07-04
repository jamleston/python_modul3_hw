def get_numbers_ticket(min, max, quantity):
    final_list = []
    if min>=1 and max>=1 and max<=1000 and quantity<=max-min+1:
        print('yay')
    else:
        print(final_list)
        return final_list
    print(final_list)
    return final_list

input_min = int(input('min: '))
input_max = int(input('max: '))
input_quantity = int(input('quantity: '))


get_numbers_ticket(input_min, input_max, input_quantity)