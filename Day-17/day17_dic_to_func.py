#!/usr/bin/env python3

def show_servers(servers):
    for server, status in servers.items():
        print(f"{server} : {status}")

server_status = {
        "web": "UP",
        "web2": "DOWN",
        "db1": "UP"
}

show_servers(server_status)

