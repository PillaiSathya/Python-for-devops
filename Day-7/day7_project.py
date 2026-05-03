#!/usr/bin/env python3

import random

# LOGIN FUNCTION
def check_login(password):
    correct_password = "admin123"

    if password == correct_password:
        return True
    else:
        return False

# RETRY LOGIN FUNCTION
def retry_login(max_attempts):
    attempts = 0

    while attempts < max_attempts:
        password = input("Enter password: ")

        if check_login(password):
            print("Login successful ✅")
            return True
        else:
            print("Wrong password ❌")
            print(f"Attempts left: {max_attempts - attempts - 1}")
        
        attempts += 1

    print("Account locked 🔒")
    return False

# Service check function
def check_service():
    status = random.choice(["down", "down", "up"])

    if status == "up":
        print("Service is UP ✅")
        return True
    else:
        print("Service is DOWN ❌")
        return False

# Main Program
print("=== DevOps Automation Script ===")

if retry_login(3):
    print("\nChecking service after login...")

    if check_service():
        print("System is ready 🚀")
    else:
        print("System has issues ⚠️ ")


