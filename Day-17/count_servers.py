#!/usr/bin/env python3

def count_servers(servers):
    return len(servers)

server_status = {
        "web1": "UP",
        "web2": "DOWN",
        "db1" : "UP"
}

total = count_servers(server_status)

print(f"Total Servers: {total}")
