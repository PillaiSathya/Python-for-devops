#!/usr/bin/env python3

def check_servers(servers):
    for server in servers:
        print(f"{server} is UP")
server_list = ["web1", "web2", "db1"]
check_servers(server_list)

