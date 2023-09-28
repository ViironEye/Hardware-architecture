def getPrecipitation(temperature, humidity):
    if humidity >= 90:
        if temperature < 0: return "Snow"
        return "Rain"
    return "Without precitipation"

temperature = float(input("Enter a temperature\n"))
humidity = float(input("Enter a humidity\n"))

print(getPrecipitation(temperature, humidity))
