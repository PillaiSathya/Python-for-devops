#!/usr/bin/env python3

import random

def check_service():
    status = random.choice(["down", "down", "up"])

    if status == "up":
        print("Service is UP ✅")
        return True
    else:
        print("Service is DOWN ❌")
        return False


def retry_service(max_attempts):
    attempts = 0

    while attempts < max_attempts:
        print(f"\nAttempt {attempts + 1}")

        if check_service():
            print("Service recovered 🎉")
            return

        attempts += 1

    print("Service failed after retries 🚨")


# MAIN PROGRAM
retry_service(5)
