"""This program will generate two random values (1-10000) using the 'random' import.
The program will use the 'add' from 'operator' import and prompt the user to input the sum of the two values.
A total of 10 iterations will occur.
"""

import random
from operator import add

for count in range(10):
    x = random.randint(1, 10000)
    y = random.randint(1, 10000)

    print("What is {} + {}? ".format(x, y))
    question = int(input())
    answer = (x + y)
    if question == answer:
        print("Well done, this is correct!")
    else:
        print("Sorry, but this is incorrect.")
