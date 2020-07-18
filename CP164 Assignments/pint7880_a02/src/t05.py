"""
------------------------------------------------------------------------
Question 5
------------------------------------------------------------------------
Author: Melissa Pinto
ID:     190647880
Email:  pint7880@mylaurier.ca
__updated__ = "2020-01-23"
------------------------------------------------------------------------
"""
import Food_utilities

max_cals = 0

origin = 1

is_veg = False

file_variable = open("foods.txt", "r")

foods = Food_utilities.read_foods(file_variable)

s = Food_utilities.food_search(foods, origin, max_cals, is_veg)

for i in s:
    print(i)