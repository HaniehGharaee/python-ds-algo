name = "hanieh"
last_name = "gharaee"
id = 13474
website = "http://www.haniehgharaee.com"

line1 = f"{'Name:':<8}{name:<15}{'Last Name:'<12}{last_name:<15}{'ID:':<4}{id}"
line2 = f"{'Web Site:':<10}{website}"

print(line1)
print(line2)

result = 4+3*5
print(result)

result1 = 5>=3
result2 = 4>20
result3 = 2>=2
print(result1)
print(result2)
print(result3)

result4 = (5>=3)and(3>100)or(4>3) #for logical conditions (recommended)
print(result4)

a = input("Enter value for a: ")
b = input("Enter value for b: ")
print("Before swapping:")
print("a =", a)
print("b =", b)
a , b = b, a 
print("After swapping:")
print("a =", a)
print("b =", b)



