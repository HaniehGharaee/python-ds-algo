# ********* if / loop / break / continue all are part of "Control Flow" *********
#Printing even number 1 to 10 in output
for k in range(1,11): #you can range(start, stop, step) -> for k in range(2, 11, 2):
    if k % 2 == 0:
        print (k)

#Read 5 number from the input and print the number of even numbers
i = 0
count = 0
while (i < 5):
    num= int(input("Enter a number:"))
    if num % 2 == 0:
        count += 1
    i += 1
print("The number of even numbers:", count)
#Divide two numbers from the input, the first by the second, using the subtraction operator instead of the division operator, and display the quotient and remainder in the output
t = int(input("Enter dividend:"))
v = int(input("Enter divisor:"))
if v == 0:
    print("Error: cannot divide by zero")
else:
    quotient = 0
    while t>= v:
        t-=v
        quotient +=1
    remainder = t
    print("quotient is ", quotient)
    print("remainder is", remainder)
# A while loop that stops when i reaches 4
print("A while loop that stops when i reaches 4")
i = 0
while(i < 12):
    print(i)
    if i == 4:
        print("Breaking from loop")
        break
    i += 1
#A loop with for ... in that stops the loop when i reaches 2
print("A loop with for ... in that stops the loop when i reaches 2")
for i in (0,1,2,3,4):
    print(i)
    if i ==2:
        break
#A loop that skips elements 2 and 4 and continues the rest of the loop
print("A loop that skips elements 2 and 4 and continues the rest of the loop")
for i in (0,1,2,3,4,5):
    if i == 2 or i == 4:
        continue
    print(i)

def break_loop():
    for i in range(1, 5):
        if(i == 2):
            return(i)
        print(i)
    return(5)
break_loop()