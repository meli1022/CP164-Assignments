"""
------------------------------------------------------------------------
Question 2
------------------------------------------------------------------------
Author: Melissa Pinto
ID:     190647880
Email:  pint7880@mylaurier.ca
__updated__ = "2020-01-30"
------------------------------------------------------------------------
"""
from Stack_array import Stack

source = Stack()

value = [1,2,3,4,5,6]

for num in value:
    source.push(num)


target1, target2 = source.split_alt()

print("target 1")
for i in target1:
    print(i)
    
print("target 2")
for i in target2:
    print(i)