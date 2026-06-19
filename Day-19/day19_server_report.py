#!/usr/bin/env python3

def save_report(servers):

    with open("server_report.log", "w") as file:

        for server, status in servers.items():
            file.write(f"{server} : {status}\n")

server_status = {
    "web1": "UP",
    "web2": "DOWN",
    "web3": "UP",
    "db1": "UP"
}

save_report(server_status)

def show_report():

    with open("server_report.log", "r") as file:
        content = file.read()

    print(content)

show_report()

def count_up_servers(servers):
    count = 0
    for server, status in servers.items():
        if status == "UP":
            count += 1
    return count

total = count_up_servers(server_status)

print(f"UP servers: {total}")


