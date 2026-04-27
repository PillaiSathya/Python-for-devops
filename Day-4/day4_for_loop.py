#!/usr/bin/env python3

names = []

while len(names) < 5:
    name = input("Enter name: ")

    if name == "":
        print("Empty input not allowed, try again!")
        continue

    if name.isdigit():
        print("Numbers are not allowed, enter a valid name!")
        continue

    if name in names:
        print("Name already entered, try different!")
        continue

    names.append(name)

print("\n--- Greetings ---")

for i, name in enumerate(names):
    print(f"{i+1}. Hello {name}")
