#Display numbers 1 to 5 in the output
# k = 0
# while(k < 5):
#     k = k + 1
#     print(k)
for k in range(1 ,6):
    print(k)
#Receive a number from input and display from 1 to the received number in output
# number = int(input("Enter a number for while:"))
# i=0
# while(i < number): # 5 < 5 is False
#     i += 1
#     print("Display Numbers:",i)
number = int(input("Enter a number for in:"))
for i in range(1, number+1):
    print(i)
#Receives a number from the input and display the sum of the numbers 1 to that number itself in the output
# num = int(input("Enter a number for while:"))
# i = 1 # or i = 0
# sum = 0
# while(i <= num):
#     sum = sum + i
#     i += 1
# print ("Sum of result the numbers", sum)
num = int(input("Enter a number for in:"))
total = 0
for i in range(1, num+1):
    total +=i
print(total)
#Receive 5 numbers from the input and print their sum and average in output
# count = 1
# total = 0
# while (count <= 5):
#     num= int(input("Enter a number:"))
#     total += num
#     count += 1
# average = total / 5
# print ("Sum of result the numbers:", total)
# print ("Average of result the numbers:", average)
total = 0
for _ in range(5):
    num= int(input("Enter a number for total and average:"))
    total += num
average = total / 5
print ("Sum of result the numbers:", total)
print ("Average of result the numbers:", average)
# Receive m numbers from the input and print their sum and average in output
total = 0
m = int(input("How many numbers?"))
for _ in range(m):
    num= int(input("Enter a number:"))
    total += num
average = total / m
print ("Sum of result the numbers:", total)
print ("Average of result the numbers:", average)
#Multiply two numbers from the first input by the second, using the addition operator instead of the multiplication operator
r = int(input("Enter a number as r:"))
s = int(input("Enter a number as s:"))
result = 0
for _ in range(s):
    result += r
print("Result:", result)