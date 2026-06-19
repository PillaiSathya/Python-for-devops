#!/usr/bin/env python3

def show_servers(servers):
    for server in servers:
        print(f"{server} is UP ✅ ")

server_list = ["web1", "web2", "web3", "db1", "db2"]
show_servers(server_list)

def count_servers(servers):
    return len(servers)

total = count_servers(server_list)

print(total)

