#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i>=0:
        if i==0:
            print("Happy New Year!")
        else:
            print(i)
        i -= 1

def square_integers(int_list):
    new_list = []
    for i in range(0,len(int_list)):
        new_list.append(int_list[i]*int_list[i])
    return new_list


def fizzbuzz():
    for i in range(1,101):
        if i%5 ==0 and i%3 ==0:
            print("FizzBuzz")
        elif i%5==0:
            print("Buzz")
        elif i%3==0:
            print("Fizz")
        else:
            print(i)
