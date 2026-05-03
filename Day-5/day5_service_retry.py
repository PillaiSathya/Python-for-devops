#!/usr/bin/env python3

import random

attempts = 0
max_attempts = int(input("Enter retry count: "))

print(f"You will retry {max_attempts} times")

while attempts < max_attempts:
    print(f"\nChecking service... Attempt {attempts + 1}")
    
    # Simulate service status (random success/failure)
    service_status = random.choice(["down", "down", "up"])

    if service_status == "up":
        print("Service is UP ✅")
        break
    else:
        print("Service is DOWN ❌")
        print(f"Retries left: {max_attempts - attempts - 1}")

    attempts += 1

if attempts == max_attempts and service_status != "up":
    print("Service is still down after retries 🚨")
