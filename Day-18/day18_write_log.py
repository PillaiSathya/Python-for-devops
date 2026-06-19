#!/usr/bin/env python3

def write_log(message):
    with open("server.log", "a") as file:
        file.write(message + "\n")

write_log("web is UP")
write_log("db1 is DOWN")


