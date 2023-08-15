#!/usr/bin/env python3

def happy_new_year():
    countdown = 10
    while countdown >= 1:
        print(countdown)
        countdown -= 1
    print("Happy New Year!")
happy_new_year()


def square_integers(int_list):
    squared_list = [n ** 2 for n in int_list]
    return squared_list
print(square_integers([1, 2, 3, 4, 5]))


def fizzbuzz():
    for num in range (100):
        if num % 15 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
fizzbuzz()