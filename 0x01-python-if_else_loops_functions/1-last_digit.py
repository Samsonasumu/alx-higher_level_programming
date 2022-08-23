#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number > 0:
    last_nm = number % 10
elif number < 0:
    last_nm = number % -10

if last_nm > 5:
    print(f"Last digit of {number} is {last_nm} and is greater than 5")
elif last_nm == 0:
    print(f"Last digit of {number} is {last_nm} and is 0")
elif last_nm < 6 and last_nm != 0:
    print(f"Last digit of {number} is {last_nm} and is less than 6 and not 0")
