#!/usr/bin/env python3

try:
    number = int(input("Enter a number: "))
    print(f"you entered: {number}")

except ValueError:
    print("Invalid Input ❌")

finally:
    print("Program finished 🚀")

