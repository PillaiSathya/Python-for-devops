#!/usr/bin/env python3

correct_password = "admin123"
attempts = 0
max_attempts = 3
logged_in = False   # 👈 new

while attempts < max_attempts:
    password = input("Enter password: ")

    if password == correct_password:
        print("Login successful ✅")
        logged_in = True
        break
    else:
        print("Wrong password ❌")
        print(f"Attempts left: {max_attempts - attempts - 1}")

    attempts += 1

if not logged_in:
    print("Account locked 🔒")
