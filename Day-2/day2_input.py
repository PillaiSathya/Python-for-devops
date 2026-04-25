#!/usr/bin/env python3

from datetime import datetime

name = input("Enter your name: ")
dob_input = input("Enter your DOB (DD/MM/YYYY): ")

# Convert string to date
dob = datetime.strptime(dob_input, "%d/%m/%Y")

today = datetime.today()

# Calculate age
age = today.year - dob.year

# Adjust if birthday not yet passed this year
if (today.month, today.day) < (dob.month, dob.day):
    age -= 1

print("\n--- DevOps Profile ---")
print(f"Name: {name}")
print(f"Current Age: {age}")
print(f"Age after 5 years: {age + 5}")
