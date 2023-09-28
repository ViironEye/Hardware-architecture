def getTime(hours):
    hours %= 24
    if hours >= 3 and hours <= 5:
        return "Early morning"
    if hours >= 6 and hours <= 10:
        return "Morning"
    if hours >= 11 and hours <= 15:
        return "Day"
    if hours >= 16 and hours <= 21:
        return "Afternoon"
    return "Night"

hours = int(input("\nEnter the hours: "))
print("\n" + getTime(hours))
