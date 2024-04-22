def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32): ")
    sort_temperature(get_user_input())

def get_user_input():
    x = input()
    numbers_list = list(map(float, x.split(", ")))
    return numbers_list

def calc_average_temeperature(sorted_list):
    print("calc_average_temperature")
    average = sum(sorted_list)
    num_elements = len(sorted_list)
    
def find_min_max():
    print("find_min_max")

def sort_temperature(temperature_list):
    print("sort_temperature")

def calc_median_temperature():
    print("calc_median_temperature")