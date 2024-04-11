#Missowina Bararmna
# 4/10/2024
# P2LAB1
# Variables Expressions
import math

# Get Radius user
radius = float(input("Enter the rdius: "))
 # Calculate Diameter, Circumference , Area of Circle
diam =  2 * radius
cir = 2 * math.pi * radius
area = math.pi * (radius **2)
# Display the result
print(f" The diameter of the cercle is {diam: .1f}")
print(f" The circumference of cercle is { cir: .2f}")
print(f" The area of the circle is { area: .3f}")
      
