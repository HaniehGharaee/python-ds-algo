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