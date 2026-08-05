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

def calculate_absolute_product(a, b):
    return abs(a) * abs(b)


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(calculate_absolute_product(a, b))

def calculate_net_salary(s):
    tax = s * 0.1
    insurance = s * 0.17
    net_salary = s - tax - insurance
    return tax, insurance, net_salary

s = int(input("Enter your salary: "))
tax, insurance, net_salary = calculate_net_salary(s)
print ("Tax:", tax)
print("insurance", insurance)
print("net_salary", net_salary)

def format_two_names_with_space (name1 , name2):
    first_message = "name: " + name1
    measure_name = len(first_message)
    if measure_name <= 30:
        calculate_space = 30 - measure_name
        second_message = " " * calculate_space  + "name: " + name2
        final_message = first_message + second_message 
        return final_message
    else: 
        return "Name is too long"
          
name1 = input("Enter your name1: ")
name2 = input("Enter your name2: ")
final_message = format_two_names_with_space(name1 , name2)
print(final_message)

def format_list_names_with_space (names):
    all_message = ""
    for i in range(0, len(names), 2):
        first_message = "name: " + names[i]
        if i+1 < len(names):
            second_message = "name: " + names[i+1]
            measure_name = len(first_message)
            if measure_name <= 30:
                calculate_space = 30 - measure_name
                line = first_message + (" " * calculate_space) + second_message 
            else: 
                return "Name is too long"
        else: 
            line = first_message
        all_message += line + "\n"
    return all_message 
            
names = ["hanieh", "maryam", "ali", "reza", "sara"]
all_message = format_list_names_with_space(names)
print(all_message)

    