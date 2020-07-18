"""
------------------------------------------------------------------------
Question 2
------------------------------------------------------------------------
Author: Melissa Pinto
ID:     190647880
Email:  pint7880@mylaurier.ca
__updated__ = "2020-01-23"
------------------------------------------------------------------------
"""
import Food_utilities

file_variable = open("foods.txt", "r")

foods = Food_utilities.read_foods(file_variable)

s = Food_utilities.average_calories(foods)

print(s)