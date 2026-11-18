# Python Fundamentals - Book Practice
# Questions 1-15

import math
import jdatetime

# Question1
print("Hello, World!")
# Question2
print("hello teacher" + "\n" + "hello student")
# Question3
name = "hanieh"
last_name = "gharaee"
id = 13474
website = "http://www.haniehgharaee.com"
print(
    f"{'name:':<5}{name:<10}{'last name:':<8}{last_name:<10}{'ID:':<3}{id}\n{'Web Site:':<8}{website}"
)
# Question4
result = 4 + 3 * 5
print("4+3*5:", result)
# Question5
result1 = 5 >= 3
result2 = 4 > 20
result3 = 2 >= 2
print(f"5>=3: {result1}\n4>20: {result2}\n2>=2: {result3}")
# Question6
result4 = (5 >= 3) and (3 > 100) or (4 > 3)  # for logical conditions (recommended)
print("(5>=3)and(3>100)or(4>3):", result4)
# Question7
a = 10
print("a =", a)
# Question8
a = 10
b = 12
print("a + b =", a + b)
# Question9
num1, num2 = map(int, input("Enter two numbers separated by space: ").split())
print("Sum", num1 + num2)
# Question10
a = int(input("Enter a for calculation:"))
calculation = (a**3) / (a * 2 + a + 1)
print("(a*a*a)/(a*a+a+1):", calculation)
# Question 10.1 - Alternative approach using math.pow
a = int(input("Enter a for calculation with math.pow:"))
calculation = math.pow(a, 3) / (math.pow(a, 2) + a + 1)
print("Calculation using math.pow():", calculation)
# Question 11
number = int(input("Enter a Ascii value:"))
print("Ascii character of", number, "is", chr(number))
# Question 12
character = input("Enter a character:")
print("Ascii value of", character, "is", ord(character))
# Question 13
a = int(input("Enter a for swapping: "))
b = int(input("Enter b for swapping: "))
print("Before swapping:")
print("a =", a)
print("b =", b)
a, b = b, a
print("After swapping:")
print("a =", a)
print("b =", b)


# Question 14
def calculate_age_in_months(year, month, day):
    # with jdatetime
    shamsi_date = jdatetime.date(year, month, day)
    miladi_date = shamsi_date.togregorian()
    today = jdatetime.date.today()
    months = (today.year - miladi_date.year) * 12 + (today.month - miladi_date.month)
    if today.day < miladi_date.day:
        months -= 1
    return months


year = int(input("Enter your birth year:"))
month = int(input("Enter your birth month:"))
day = int(input("Enter your birth day:"))
age_in_months = calculate_age_in_months(year, month, day)
print("You have lived", age_in_months, "months")


# Question 15
def calculate_absolute_product(a, b):
    return abs(a) * abs(b)
    # abs_First_Number = abs(a)
    # abs_Second_Number = abs(b)
    # result = abs_First_Number * abs_Second_Number
    # return result


a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
print(calculate_absolute_product(a, b))
