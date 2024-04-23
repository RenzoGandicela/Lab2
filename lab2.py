def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    sorted_list = sort_temperature(num_list)
    print("Average = " + str(calc_average_temperature(num_list)))
    find_min_max(sorted_list)
    print("Median = " + str(calc_median_temperature(sorted_list)))

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32): ")

def get_user_input():
    x = input()
    num_list = list(map(float, x.split(", ")))
    return num_list

def calc_average_temperature(sorted_list):
    total = sum(sorted_list)
    num_elements = len(sorted_list)
    average = total/num_elements
    return average
    
def find_min_max(sorted_list):
    print("Min. = " + str(sorted_list[0]))
    print("Max. = " + str(sorted_list[-1]))

def sort_temperature(num_list):
    sorted_list = sorted(num_list)  #sorted() func sorts items in a list in ascending order
    return sorted_list

def calc_median_temperature(sorted_list):
    n = len(sorted_list)
    if n % 2 == 1: # Odd number of elements: return the middle element
        median = sorted_list[n//2]
    else: # Even number of elements: return the average of the middle two elements
        median = (sorted_list[(n//2)-1] + sorted_list[n//2]) / 2
    return median

if __name__ == "__main__" :
    main()