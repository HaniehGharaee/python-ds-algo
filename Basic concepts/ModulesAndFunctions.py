from datetime import date
import math
calculate = math.sqrt(16)
print(calculate)

def sayHello():
    """This is the module docstring."""
    return 'Hello World'
print(sayHello())

def say_hello():
    print("Hello!")
say_hello()

def sum_of_numbers(a, b):
    result = a + b
    return result
print(sum_of_numbers(20, 30))

def result_Operation(a):
    print("enter a: ", a)
    result = (a ** 3) / (a ** 2 + a + 1)
    return result
print(result_Operation(3))

def calculate_age_in_months(year, month, day):
    birth_date =  date(year, month, day)
    today = date.today()
    months = (today.year - birth_date.year) * 12 + (today.month - birth_date.month) 
    if today.day < birth_date.day : 
        months -= 1
        return months
    
year = int(input("Enter your birth year:"))
month = int(input("Enter your birth month:"))
day = int(input("Enter your birth day:"))
age_in_months = calculate_age_in_months(year, month, day)
print("You have lived", age_in_months, "months")

def calculate_absolute_product(a , b):
    return abs(a) * abs(b)
    # abs_First_Number = abs(a)
    # abs_Second_Number = abs(b)
    # result = abs_First_Number * abs_Second_Number
    # return result
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
print(calculate_absolute_product(a , b))
    