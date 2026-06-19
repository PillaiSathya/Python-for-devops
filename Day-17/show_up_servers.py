#!/usr/bin/env python3

def show_up_servers(servers):
    for server, status in servers.items():
        if status == "UP":
            print(server)

server_status = {
    "web1": "UP",
    "web2": "DOWN",
    "db1":  "UP"
 }

show_up_servers(server_status)
