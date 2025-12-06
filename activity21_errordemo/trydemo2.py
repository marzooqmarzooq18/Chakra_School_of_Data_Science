try:
    num1 = int(input("enter first number"))
    num2 = int(input("enter second number"))
    result = num1 / num2
    print("the result is", result)


except ZeroDivisionError:
    print("Division by zero is not allowed")

except ValueError:
    print("Please enter Numbers Only")