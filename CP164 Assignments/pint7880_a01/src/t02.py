"""
------------------------------------------------------------------------
Question 2
------------------------------------------------------------------------
Author: Melissa Pinto
ID:     190647880
Email:  pint7880@mylaurier.ca
__updated__ = "2020-01-15"
------------------------------------------------------------------------
"""
import functions


name = input()

while name!= "":
    valid = functions.is_valid(name)
    print("{}:{}".format(name,valid))
    name = input()