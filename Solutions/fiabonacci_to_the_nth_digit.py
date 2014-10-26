"""Fibonacci Sequence - Enter a number and
have the program generate the Fibonacci
sequence to that number or to the Nth number."""

# Import the math module
import math

# Ask until where the Fibonacci suit should go
precision = int(
    raw_input("\nHow far would you like to discover the Fibonacci suit ? >>"))
x = 1
i = 0
# Define limit.
while precision > 100:
    print(
        "\nSorry, but you're going too far... Besides, what the hell do you need so many numbers for ?")
    precision = int(
        raw_input("How far would you like to discover the Fibonacci suit ? >>"))
else:
    # This prints the Fibonacci suit, wich is the sum of the two last numbers.
    while i < precision:
        x = x + x
        i = i + 1
        print(x)
    if precision > 50:
        print("\nWhat the hell do you need so many numbers for ?")
