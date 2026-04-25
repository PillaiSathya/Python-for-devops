#!/usr/bin/env python3

from datetime import datetime

name = input("Enter your name: ")
dob_input = input("Enter your DOB (DD/MM/YYYY): ")

dob = datetime.strptime(dob_input, "%d/%m/%Y")
today = datetime.today()

age = today.year - dob.year

if (today.month, today.day) < (dob.month, dob.day):
    age -= 1

print("\n--- DevOps Profile ---")
print(f"Name: {name}")
print(f"Age: {age}")

# Decision logic
if age < 25:
    print("You are early in your career 🚀")
elif age >= 25 and age < 35:
    print("Perfect time to grow strong in DevOps 💪")
else:
    print("Great experience, time to aim for senior roles 🔥")
if age >= 30:
    print("Target: Senior DevOps Engineer roles soon!")
else:
    print("Focus on strong fundamentals!")
