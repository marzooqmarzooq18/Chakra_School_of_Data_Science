try:
    num1 = int(input("enter first number"))
    num2 = int(input("enter second number"))
    result = num1 / num2
    print("the result is", result)

except (ValueError, ZeroDivisionError):
    print("Invalid input or division by zero")

else:
    print("Result is", result)

finally:
    print("Program is executed")