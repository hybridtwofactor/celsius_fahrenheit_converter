Goal
---
Write a program that converts celsius temperatures to fahrenheit temperatures and vice versa.

Research
---
Source: https://www.almanac.com/temperature-conversion-celsius-fahrenheit

Celsius to Fahrenheit
- multiply by 1.8 (9/5) and add 32
- (celsius number * 1.8) + 32

Fahrenheit to Celsius
- subtract 32 and multiply by .5556 (5/9)
- (fahrenheit number - 32) * 0.5556
- The number 0.5556 is a rounded number to 4dp

Plan
---
- user will choose the type of temperature to convert (celsius or fahrenheit)
- user enter the number as input
- output will be the conversion of the other temperature type equal to the input number of the chosen temperature type

Pseudocode
---
<br>user inputs the letter options - c or f
<br>if "c"
<br>enter the number
<br>&emsp;    call function to convert celsius to fahrenheit
<br>&emsp;    return output value
<br>else if "f"
<br>&emsp;    call function to convert fahrenheit to celsius
<br>&emsp;    return output value

function celsius to fahrenheit
<br>&emsp;    return (celsius number * 1.8) + 32

function fahrenheit to celsius
<br>&emsp;    return (fahrenheit number - 32) * 5 / 9

Now we shall code!
