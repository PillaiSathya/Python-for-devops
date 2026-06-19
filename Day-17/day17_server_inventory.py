#!/usr/bin/env python3

def show_servers(servers):
    for server, status in servers.items():
        print(f"{server} : {status}")

server_status = {
    "web1": "UP",
    "web2": "DOWN",
    "web3": "UP",
    "db1": "UP",
    "db2": "DOWN"
}

show_servers(server_status)


def count_servers(servers):
    return len(servers)

total = count_servers(server_status)
print(f"Total Servers : {total}")

def show_up_servers(servers):
    for server, status in servers.items():
        if status == "UP":
            print(f"up_servers: {server}")

show_up_servers(server_status)

def show_down_servers(servers):
    for server, status in servers.items():
        if status == "DOWN":
            print(f"down_servers: {server}")

show_down_servers(server_status)

