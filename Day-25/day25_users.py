#!/usr/bin/env python3

users = {
    "sathya": "admin",
    "john": "developer",
    "alice": "tester"
 }

user_name = input("Enter username:")

Role = users.get(user_name, "user not found")

print("Role:", Role)

