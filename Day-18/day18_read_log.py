#!/usr/bin/env python3

def read_log():

    with open("server.log", "r") as file:
        content = file.read()

    print(content)

read_log()

