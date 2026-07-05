#!/usr/bin/env python3

def get_server_status(servers, server):
    for server_name, status in servers.items():
        if server_name == server:
            return f"{server} is {status}"
        
    return "Server not found"

server = input("Enter server name: ")

servers = {
    "web1": "UP",
    "web2": "DOWN",
    "db1": "UP"
}

result = get_server_status(servers, server)
print(result)

