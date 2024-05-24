#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if (username.lower() == "admin") and (password == "12345"):
        print("Access Granted")
    else:
        print("Access Denied")
admin_login("admiN", "12345")

def hows_the_weather(temperature):
    # your code here
    if temperature < 40:
        print("It's brisk out there!")
    elif ((temperature == 40) and (temperature == 65)):
        print("It's a little chilly out there!")
    elif temperature > 85:
        print("It's too dang hot out there!")
    else:
        print("It's perfect out there!")

hows_the_weather(temperature = 86)


def fizzbuzz(num):
    # your code here
    for i in num ( num % 3 == 0 ):
        print("Fizz")
    for i in num ( num % 5 == 0 ):
        print("Buzz")
    for i in num (( num % 3 == 0 ) and ( num % 5 == 0 )):
        print("FizzBuzz")

def calculator(operation, num1, num2):
    # your code here
    pass
