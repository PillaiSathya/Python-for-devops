#!/usr/bin/env python3

def save_status(servers):
    with open("inventory.log", "w") as file:
        for server, status in servers.items():
            file.write(f"{server} : {status}\n")

server_status = {
        "web1": "UP",
        "web2": "DOWN",
        "db1": "UP"
}

save_status(server_status)
