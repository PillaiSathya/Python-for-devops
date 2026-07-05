#!/usr/bin/env python3

servers = {
    "web1": "UP",
    "web2": "DOWN",
    "db1": "UP"
}

server = input("Enter server name: ")

status = servers.get(server, "Server not found")

print(status)
