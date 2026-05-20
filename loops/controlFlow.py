# ********* if / loop / break / continue all are part of "Control Flow" *********
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