#Display numbers 1 to 5 in the output
k = 0
while(k < 5):
    k = k + 1
    print(k)
#Receives a number from the input and display the sum of the numbers 1 to that number itself in the output
num = int(input("Enter a number:"))
i = 1 # or i = 0
sum = 0
while(i <= num):
    sum = sum + i
    i += 1
    
print ("Sum of result the numbers", sum)
#Receive 5 numbers from the input and print their sum and average in output
count = 1
total = 0
while (count <= 5):
    num= int(input("Enter a number:"))
    total += num
    count += 1
average = total / 5
print ("Sum of result the numbers:", total)
print ("Average of result the numbers:", average)
# Receive m numbers from the input and print their sum and average in output
count = 1
total = 0
m = int(input("How many numbers?"))
while (count <= m):
    num= int(input("Enter a number:"))
    total += num
    count += 1
average = total / m
print ("Sum of result the numbers:", total)
print ("Average of result the numbers:", average)