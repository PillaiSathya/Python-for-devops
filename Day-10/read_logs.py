#!/usr/bin/env python3

log_file = open("server.log", "r")

content = log_file.read()

print(content)

log_file.close()
