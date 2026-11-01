# Question1
print("Hello, World!")
# Question2
print("hello teacher" + "\n" + "hello student")
# Question3
name = "hanieh"
last_name = "gharaee"
id = 13474
website = "http://www.haniehgharaee.com"
print(f"{'name:':<5}{name:<10}{'last name:':<8}{last_name:<10}{'ID:':<3}{id}\n{'Web Site:':<8}{website}")
# Question4
result = 4+3*5
print(result)
# Question5
result1 = 5>=3
result2 = 4>20
result3 = 2>=2
print(f"{result1}\n{result2}\n{result3}")
# Question6
result4 = (5>=3)and(3>100)or(4>3) #for logical conditions (recommended)
print(result4)
# Question7
a = 10 
print(a)
# Question8
a = input("Enter value for a: ")
b = input("Enter value for b: ")
print("Before swapping:")
print("a =", a)
print("b =", b)
a , b = b, a 
print("After swapping:")
print("a =", a)
print("b =", b)

# input and output
age, height, grade, name = input("Enter your age, height, grade, and name: ").split(",")
age = int(age)
height = float(height)
grade = grade
name = str(name)
print("Your age:", age)
print("Your height:", height)
print("Your grade:", grade)
print("Your name:", name)
