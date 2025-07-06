print("FIRST CALCULATOR")

start = 1

while start == 1:

    x = float(input("What´s x? "))
    y = float(input("What´s y? "))
    operator = input("Enter operator + - / // % * **")

    if operator == "+":
        result = x + y
    elif operator == "-":
        result = x - y
    elif operator == "*":
        result = x * y
    elif operator == "**":
        result = x ** y
    elif operator == "/":
        if y != 0:
            result = x / y
        else:
            result = "Error: Division by zero"
    elif operator == "//":
        if y != 0:
            result = x // y
        else:
            result = "Error: Division by zero"
    elif operator == "%":
        if y != 0:
            result = x % y
        else:
            result = "Error: Division by zero"
    else:
        result = "Invalid operator"

    print("Result: ", result)
    
    start = int(input("If you want to perform another operation press one, if you want to turn off the calculator press zero: "))




