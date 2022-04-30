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


match operation:
    case "+":
        add()
        valid = True

    case "-":
        sub()
        valid = True
    case "*":
        mul()
        valid = True
    case "/":
        div()
        valid = True
    case "^":
        exp()
if valid:
    sys.quit()
elif not valid:
    sys.exit("Fatal Error: Invalid Input! Error Code 1 :(")
else:
    sys.exit("Fatal Error: Corrupted variable('valid')! Error Code 2 :()")
