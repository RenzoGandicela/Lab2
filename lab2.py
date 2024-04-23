def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32): ")
    num_list = get_user_input()
    sorted_list = sort_temperature(num_list)
    calc_average_temperature(num_list)
    find_min_max(sorted_list)

def get_user_input():
    x = input()
    numbers_list = list(map(float, x.split(", ")))
    return numbers_list

def calc_average_temperature(sorted_list):
    total = sum(sorted_list)
    num_elements = len(sorted_list)
    average = total/num_elements
    return average
    
def find_min_max(sorted_list):
    print("Min. = " + sorted_list[0])

def sort_temperature(num_list):
    sorted_list = sorted(num_list)
    return sorted_list

def calc_median_temperature():
    print("calc_median_temperature")