"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Melissa Pinto
ID:     190647880
Email:  pint7880@mylaurier.ca
__updated__ = "2020-03-05"
------------------------------------------------------------------------
"""

from Sorted_List_linked import Sorted_List

self = Sorted_List()


value = 2
Sorted_List.insert(self, value)
value = 3
Sorted_List.insert(self, value)
value = 2
Sorted_List.insert(self, value)

key = 2

p= Sorted_List.find(self, key)

print(p)



