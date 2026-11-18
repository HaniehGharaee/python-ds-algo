#Determine whether the number received from the input is even or odd?
number = int(input("Enter a number:"))
if number%2 == 0:
    print(number, "is an even")
else:
    print(number, "is an odd")
#####################################################
def printNumber(number):
    if number%2 == 0:
        print(number, "is an even")
    else:
        print(number, "is an odd")
z = 5
printNumber(z)
###################################################################################################
#Read the sides of a triangle from the input and determine the largest one.
a = int(input("Enter a number as a:"))
b = int(input("Enter a number as b:"))
c = int(input("Enter a number as c:"))
greatest = max(a,b,c)
print (greatest, "is the greatest number")

#Read the side of a triangle from the input. If the triangle is right-angled, a message is output.
x = int(input("Enter a number as x:"))
y = int(input("Enter a number as y:"))
z = int(input("Enter a number as z:"))
if x*x == y*y + z*z:
    print("Right angled")
elif y*y == x*x + z*z:
    print("Right angled")
elif z*z == x*x + y*y:
    print("Right angled")
else:
    print("not Right angled")

#Receive a number from the input. 
# If the number is 1, the first message is printed. 
# If the number is 2, the second message is printed. 
# If the number is 3, the third message is printed.
#  Otherwise, the desired message is printed.
r = int(input("Enter a number as r:"))
if r==1:
    print ("one")
elif r==2:
    print ("two")
elif r==3:
    print ("three")
else:
    print ("other")