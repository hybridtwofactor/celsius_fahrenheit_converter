# function convert celsius to fahrenheit 
def celsius_to_fahrenheit(number):
    return (number * 1.8) + 32

# function convert fahrenheit to celsius 
def fahrenheit_to_celsius(number):
    return (number - 32) * 5 / 9
    
    
# get user input of temperature type to convert to
choice = input("Convert celsius [c] or fahrenheit [f]: ")
# get user input of the temperature value
number = int(input("Enter the number: "))

# outputting the temperature conversion
if choice == "c":
    print("Fahrenheit:", celsius_to_fahrenheit(number), "degrees")
elif choice == "f":
    print("Celsius:", fahrenheit_to_celsius(number), "degrees")



# testing
print()
print("testing area below")
print("------------------")
print("testing celsius to fahrenheit function")
print(celsius_to_fahrenheit(18))
print(celsius_to_fahrenheit(1))
print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(-1))
print(celsius_to_fahrenheit(-52))

print("testing fahrenheit to celsius function")
print(fahrenheit_to_celsius(162))
print(fahrenheit_to_celsius(1))
print(fahrenheit_to_celsius(0))
print(fahrenheit_to_celsius(-1))
print(fahrenheit_to_celsius(-98))