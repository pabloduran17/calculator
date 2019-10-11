num1 = int(input("Write a number"))
num2 = int(input("Write other number"))
sol = str(input("Choose the operation: +, -, * or /"))
if sol == "+":
    print(num1 + num2)
elif sol == "-":
    print(num1 - num2)
elif sol == "*":
    print(num1 * num2)
elif sol == "/":
    print(num1 / num2)
else:
    print("sorry boss..")