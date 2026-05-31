#!/usr/bin/env python3

try:
    age = int(input("Enter your age: "))

    print(f"Your age is {age}")

except ValueError:
    print("Only numbers are allowed ❌")
