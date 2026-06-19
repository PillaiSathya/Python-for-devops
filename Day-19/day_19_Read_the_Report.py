#!/usr/bin/env python3

def show_report():
    with open("inventory.log", "r") as file:
        content = file.read()
    print(content)
show_report()
