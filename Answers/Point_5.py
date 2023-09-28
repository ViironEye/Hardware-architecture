password = input("Enter your password: ")
hasUpper = False
hasLower = False
hasDigit = False
for i in range(len(password)):
    if password[i] >= 'A' and password[i] <= 'Z':
        hasUpper = True
    if password[i] >= 'a' and password[i] <= 'z':
        hasLower = True
    if password[i] >= '0' and password[i] <= '9':
        hasDigit = True

if len(password) >= 4 and hasUpper and hasLower and hasDigit:
    print("Correct password!")
else:
    print("\nToo short password" if len(password) < 4 else "", end="")
    print("\nHas no uppercase numbers" if not hasUpper else "", end="")
    print("\nHas no lowercase numbers" if not hasLower else "", end="")
    print("\nHas no digits" if not hasDigit else "")
