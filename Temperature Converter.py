print(" Temperature Converter ")
print()
Celcius = float(input('enter the temperature in Celcius : '))
"""
Fahrenheit to Celcius: C = (F-32) (5/9)
Celsius to Fahrenheit: F = C(9/5) + 32
"""
Fahrenheit = (9/5)*Celcius + 32
print()
print(f"{Celcius} Celsius to Fahrenheit is : {Fahrenheit:.2f} F")
print()
