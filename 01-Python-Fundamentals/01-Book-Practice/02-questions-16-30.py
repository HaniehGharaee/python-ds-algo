# Python Fundamentals - Book Practice
# Questions 16-30
import math


# Question 16
def convert_shamsi_year_to_gregorian(shamsi_year):
    gregorian_year = shamsi_year + 621
    return gregorian_year


shamsi_year = int(input("Enter a Shamsi year:"))
gregorian_year = convert_shamsi_year_to_gregorian(shamsi_year)
print("The corresponding Gregorian year is:", gregorian_year)


# Question 17
def calculate_net_salary(s):
    tax = s * 0.1
    insurance = s * 0.17
    net_salary = s - tax - insurance
    return tax, insurance, net_salary


s = int(input("Enter your salary: "))
tax, insurance, net_salary = calculate_net_salary(s)
print("Tax:", tax)
print("insurance", insurance)
print("net_salary", net_salary)

# Question 18
name1 = input("Enter name: ")
name2 = input("Enter name: ")
first_message = "name: " + name1
second_message = "name: " + name2
print(first_message + " " * 30 + second_message)


def format_list_names_with_space(namesList):
    all_message = ""
    for i in range(0, len(namesList), 2):
        first_message = "name: " + namesList[i]
        if i + 1 < len(namesList):
            second_message = "name: " + namesList[i + 1]
            line = first_message.ljust(30) + second_message
        else:
            line = first_message
        all_message += line + "\n"
    return all_message


namesList = ["hanieh", "maryam", "ali", "reza", "sara", "mohammad"]
all_message = format_list_names_with_space(namesList)
print(all_message)


# Question 19
def calculate_circle_area(radius):
    area = math.pi * radius**2
    return area


radius = float(input("Enter the radius of the circle:"))
area = calculate_circle_area(radius)
print("The area of the circle is:", area)
