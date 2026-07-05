#!/usr/bin/env python3

servers = {
    "web1": "UP",
    "web2": "DOWN",
    "db1": "UP",
    "db2": "DOWN"
 }

server = input("Enter server name: ")
status = servers.get(server, "Server not found")
print(status)
