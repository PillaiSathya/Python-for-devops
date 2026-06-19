#!/usr/bin/env python3

def check_server_health(servers):
    for server, status in servers.items():

        if status == "UP":
            print(f"✅ {server} is healthy")

        else:
            print(f"❌ {server} needs attention")

server_status = {
    "web1": "UP",
    "web2": "DOWN",
    "db1": "UP"
}

check_server_health(server_status)

