#!/usr/bin/env python3

names = []

for i in range(5):
    server_name = input("Enter server_name: ")
    names.append(server_name)

print("\n---Server List---")

for index, server_name in enumerate(names, start=1):
    print(f"{index}. {server_name}")