"""This program will generate a list of 30 random numbers (from 1 - 99) using the 'random' import.
It will then print the list of randomly generated numbers and a list of numbers that were repeated during generation
"""

import random

list = []
while True:
    rand_int = random.randint(1, 100)
    list.append(rand_int)

    if len(list) >= 30:
        break

randTuple = tuple(list)

print('Random list:', randTuple)
print('Repeated numbers:', set([x for x in randTuple if randTuple.count(x) > 1]))