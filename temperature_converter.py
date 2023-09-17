# function convert celsius to fahrenheit 
def celsius_to_fahrenheit(number):
    return (number * 1.8) + 32

# function convert fahrenheit to celsius 
def fahrenheit_to_celsius(number):
    return (number - 32) * 5 / 9

# function check if input is a float
def is_float(string):
    try:
        float(string)
        return True
    except:
        return False


# get user input of temperature type to convert
choice = input("Convert celsius [c] or fahrenheit [f]: ")
while choice not in ["c", "f", "C", "F"]:
    print("Invalid input. Please enter your option again.")
    choice = input("Convert celsius [c] or fahrenheit [f]: ")

# get user input of the temperature value
number = input("Enter the number: ")
while is_float(number) == False:
    print("Invalid input. Please enter number again.")
    number = input("Enter the number: ")
number = float(number)

# outputting the temperature conversion
if choice == "c" or choice == "C":
    print()
    print("Result", celsius_to_fahrenheit(number), "degrees fahrenheit")
elif choice == "f" or choice == "F":
    print()
    print("Result", fahrenheit_to_celsius(number), "degrees celsius")



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