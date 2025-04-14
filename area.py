import math

# Function definitions
def triangle(base, height):
    return (base * height) / 2

def rectangle(length, width):
    return length * width

def square(side):
    return pow(side, 2)

def circle(radius):
    return math.pi * pow(radius, 2)

# Input validation helpers
def get_valid_choice():
    while True:
        try:
            choice = int(input('Which shape: '))
            if 1 <= choice <= 5:
                return choice
            else:
                print("Please enter a number from 1 to 5.")
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 5.")

def get_positive_number(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Main program
print('==================\nArea Calculator 📐\n==================')
print('1) Triangle\n2) Rectangle\n3) Square\n4) Circle\n5) Quit')

shape = get_valid_choice()

if shape == 1:
    base = get_positive_number('\nBase: ')
    height = get_positive_number('Height: ')
    print('\nThe area is', triangle(base, height))

elif shape == 2:
    length = get_positive_number('\nLength: ')
    width = get_positive_number('Width: ')
    print('\nThe area is', rectangle(length, width))

elif shape == 3:
    side = get_positive_number('\nSide: ')
    print('\nThe area is', square(side))

elif shape == 4:
    radius = get_positive_number('\nRadius: ')
    print('\nThe area is', circle(radius))

else:
    print('\nNo shape was given')
