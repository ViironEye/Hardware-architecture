def divisionResult(num1, num2):
    return "Error" if num1 == 0 or num2 == 0 else str(round(num1 / num2, 4))

num1 = float(input("\nEnter the first number: "))
num2 = float(input("\nEnter the second number: "))
if not divisionResult(num1, num2) == "Error":
    print("\nResult 1: " + divisionResult(num1, num2))
    print("\nResult 2: " + divisionResult(num2, num1))
else :
    print("\n\tDivision by zero exception!")
