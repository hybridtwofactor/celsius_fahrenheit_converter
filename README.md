Goal: Write a program that converts celsius temperatures to fahrenheit temperatures and vice versa.

Research
----------
Source: https://www.almanac.com/temperature-conversion-celsius-fahrenheit

Celsius to Fahrenheit
- multiply by 1.8 (9/5) and add 32
- (celsius number * 1.8) + 32

Fahrenheit to Celsius
- subtract 32 and multiply by .5556 (5/9)
- (fahrenheit number - 32) * 0.5556
- The number 0.5556 is a rounded number to 4dp

Plan
- user will choose the type of temperature to convert (celsius or fahrenheit)
- user enter the number as input
- output will be the conversion of the other temperature type equal to the input number of the chosen temperature type

Pseudocode
user inputs the letter options - c or f
if "c"
    call function to convert celsius to fahrenheit
    return output value
else if "f"
    call function to convert fahrenheit to celsius
    return output value

function celsius to fahrenheit
    return (celsius number * 1.8) + 32

funciton fahrenheit to celsius
    return (fahrenheit number - 32) * 5 / 9

Now we shall code!