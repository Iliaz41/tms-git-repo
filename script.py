import random

def check_even_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

random_number = random.randint(1, 100)
print(f"Generated number: {random_number}")
print(f"The number is {check_even_odd(random_number)}.")
