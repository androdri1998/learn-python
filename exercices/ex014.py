degrees_celsius_value = input("What's the temperature? °C ")

try:
    degrees_celsius = float(degrees_celsius_value)
    degrees_fahrenheit = ((9 * degrees_celsius) / 5) + 32

    print("{:.1f}°C is equal to {:.1f}°F".format(
        degrees_celsius, degrees_fahrenheit))
except ValueError:
    print("It isn't a number")
