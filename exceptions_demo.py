"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
   Answer: A ValueError will occur when the user inputs a value that cannot be converted to an integer using int().

2. When will a ZeroDivisionError occur?
   Answer: A ZeroDivisionError will occur when the user inputs 0 as the denominator, resulting in division by zero.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
   Answer: Yes, we can change the code to avoid the possibility of a ZeroDivisionError by checking if the denominator is zero before performing the division operation.

"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")
