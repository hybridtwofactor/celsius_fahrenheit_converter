def celsius_to_fahrenheit(number):
    return (number * 1.8) + 32

def fahrenheit_to_celsius(number):
    return (number - 32) * 5 / 9

# testing
print(celsius_to_fahrenheit(18))
print(celsius_to_fahrenheit(1))
print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(-1))
print(celsius_to_fahrenheit(-52))

print(fahrenheit_to_celsius(162))
print(fahrenheit_to_celsius(1))
print(fahrenheit_to_celsius(0))
print(fahrenheit_to_celsius(-1))
print(fahrenheit_to_celsius(-98))