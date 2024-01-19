# use_cases/generate_random_number.py

from entities.random_number import RandomNumber
import random

def generate_random_number():
    value = random.randint(1, 15)
    return RandomNumber(value)
