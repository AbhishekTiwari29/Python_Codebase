temperature = int(input("Enter Temperature: "))
humidity = int(input("Enter Humidity: "))

if temperature >= 30 and humidity >= 90:
    print("Weather is: Hot and Humid")
elif temperature >= 30 and humidity < 90:
    print("Weather is: Hot")
elif temperature < 30 and humidity >= 90:
    print("Weather is: Cool and Humid")
else:
    print("Weather is: Cool")
