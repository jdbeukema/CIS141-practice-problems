# 1. Create a program that prints the following output to the screen: "Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked."
print("Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked.")
print("")

# 2. Create a program that prompts for 2 numbers and then outputs the addition, subtraction, multiplication, and division of the first number by the second number.
num1 = float(input("Please choose a number: "))
num2 = float(input("Please choose a number: "))
result1 = num1 + num2
result2 = num1 - num2
result3 = num1 * num2
result4 = num1 / num2
print(num1," + ",num2," = ",result1)
print(num1," - ",num2," = ",result2)
print(num1," x ",num2," = ",result3)
print(num1," ÷ ",num2," = ",result4)
print("")

# 3. Create a program that prompts for the side lengths of a triangle and computes the area using Heron's formula. (https://en.wikipedia.org/wiki/Heron%27s_formula)
a = float(input("What is the length of the first side of the triangle? "))
b = float(input("What is the length of the second side of the triangle? "))
c = float(input("What is the length of the third side of the triangle? "))
p=(a+b+c)
s=p/2
area = (s*(s-a)*(s-b)*(s-c))**0.5

print("The area of the triangle is ",area)

print("")

# 4. Create a program that computes different statistics given five numbers including the total, average, minimum, maximum, range, and standard deviation (https://en.wikipedia.org/wiki/Standard_deviation).
import statistics

numbers = [3,.44,500,-125,66]
print(numbers)
print("Total is ",sum(numbers))
#print("Average is ",mean(numbers))
#print("Smalest is ",math.floor(numbers))
#print("Largestest is ",math.ceil(numbers))
#print("Range is ",range(numbers))
print("Standard deviation is ",statistics.stdev(numbers))

print("")
