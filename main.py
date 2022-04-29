import sys
import tkinter as tk

first_number: float = 0.0
second_number: float = 0.0
operation: str = " "
sum: float = 0.0
difference: float = 0.0
product: float = 0.0
dividend: float = 0.0
valid: bool = False
finished: float = 0.0

window = tk.Tk()

def add():
    first_number = float(input("First Number: "))
    second_number = float(input("Second Number: "))
    sum: float = first_number + second_number
    print(sum)


def exp():
    first_number: float = float(input("First Number: "))
    second_number: float = float(input("Second Number: "))
    finished: float = first_number ** second_number
    print(finished)


def sub():
    first_number: float = float(input("First Number: "))
    second_number: float = float(input("Second Number: "))
    difference: float = first_number - second_number
    print(difference)


def mul():
    first_number: float = float(input("First Number: "))
    second_number: float = float(input("Second Number: "))
    product: float = first_number * second_number
    print(product)


def div():
    first_number: float = float(input("First Number: "))
    second_number: float = float(input("Second Number: "))
    dividend: float = first_number / second_number
    print(dividend)


# operation selection
operation = input("enter operation (+ - / * ^): ")
if "+" in operation:
    add()
    Valid = True
elif "-" in operation:
    sub()
    valid = True
elif "*" in operation:
    mul()
    valid = True
elif "/" in operation:
    div()
    valid = True
elif "^" in operation:
    exp()
    valid = True
else:
    sys.exit("Fatal Error: Invalid Input! Error Code 1 :(")
