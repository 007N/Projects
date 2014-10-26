# Collatz Conjecture - Start with a number n > 1.
# Find the number of steps it takes to reach one using the following process:
# If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.
import time

number_steps = 0

user_input = int(raw_input("Please enter a valid number greater than 1. >> "))
while 1 >= user_input:
    user_input = int(
        raw_input("Please enter a valid number greater than 1. >> "))

if user_input % 2 != 0:
    while user_input != 1 and user_input % 2 != 0:
        user_input = (user_input * 3) + 1
        number_steps += 1
    else:
        while user_input != 1:
            user_input = user_input / 2
            number_steps += 1


else:
    while user_input != 1:
        user_input = user_input / 2
        number_steps += 1

print('We needed ', number_steps, ' steps to arrive at 1 using that number.')
