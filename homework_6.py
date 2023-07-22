# 1. Write a Python program to compute the difference between two lists. Don`t use sets here 1. Write a Python program to compute the difference between two lists. Don`t use sets here


list_1 = ['a', 'b', 'c', 'd']
list_2 = ['c', 'd', 'e']

def compute_difference(first: list, second: list) -> tuple:
    first_second = [item for item in first if item not in second]
    second_first = [item for item in second if item not in first]
    print("first-second:", first_second)
    print("second_first:", second_first)
    return

compute_difference(list_1, list_2)



# 2. 
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.


nums = [1, 2, 3, 4, 5]
target = 7

def sum_of_two(nums: list, target: int) -> list:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):  
            if nums[i] + nums[j] == target:
                return [i, j] 
    return [] 

indices = sum_of_two(nums, target)
print("Indices:", indices, "doing target: ", target)



# 3. Write a program that takes a list of integers as input and returns a new list that contains only the elements that are unique (i.e., that appear only once in the list).



arr = [1, 2, 3, 3, 4, 4, 5]

def unique_elements(arr: list) -> list:
    unique_elements = []
    for num in arr:
        if arr.count(num) == 1:
            unique_elements.append(num)
    return unique_elements

print(unique_elements(arr))



# 4. Write a program that takes a list of integers as input and returns a new list that contains only the elements that appear an odd number of times in the list.



arr_list = [1, 1, 2, 3, 3, 3, 4, 5, 5]

def odd_elements(arr_list: list) -> list:
    odd_elements = []
    for num in arr_list:
        if arr_list.count(num) % 2 != 0:
            odd_elements.append(num)
    return odd_elements

result = odd_elements(arr_list)
print(result)


# 5. Write a program that takes a list of integers as input and returns the second-largest element in the list. If the list has fewer than two elements, the program should return None.



input_list = [1, 2, 8, 2, 5, 11]
def second_largest_element(arr: list) -> int:
    if len(arr) < 2:
        return None
    
    max_num = max(arr)
    second_num = float("-inf")
    
    for num in arr:
        if num > second_num and num < max_num:
            second_num = num
    
    return second_num
result = second_largest_element(input_list)
print(result)




# 6. Sort the following list by population. Calculate average and total population for cities from this list:


city_populations = [

    ('New York City', 8550405),

    ('Los Angeles', 3792621),

    ('Chicago', 2695598),

    ('Houston', 2100263),

    ('Philadelphia', 1526006),

    ('Phoenix', 1445632),

    ('San Antonio', 1327407),

    ('San Diego', 1307402),

    ('Dallas', 1197816),

    ('San Jose', 945942),

]
sorted_cities = sorted(city_populations, key=lambda x: x[1])
total_population = sum(city[1] for city in city_populations)
average_population = total_population / len(city_populations)
for city in sorted_cities:
    print(city[0])
print("Popolazione totale delle città:", total_population)
print("Popolazione media delle città:", average_population)