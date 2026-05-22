#!/usr/bin/env python3

import random

# ---------------------------
# USER DETAILS
# ---------------------------

name = input("Enter your name: ")
role = input("Enter your role: ")

print(f"\nHello {name}, welcome {role} 🚀")


# ---------------------------
# LOGIN SYSTEM
# ---------------------------

correct_password = "devops123"
attempts = 0
max_attempts = 3
logged_in = False

while attempts < max_attempts:

    password = input("\nEnter password: ")

    if password == correct_password:
        print("Login successful ✅")
        logged_in = True
        break

    else:
        print("Wrong password ❌")
        print(f"Attempts left: {max_attempts - attempts - 1}")

    attempts += 1


# ---------------------------
# IF LOGIN FAILED
# ---------------------------

if not logged_in:
    print("Account locked 🔒")

else:

    # ---------------------------
    # SERVER LIST
    # ---------------------------

    servers = []

    while len(servers) < 3:

        server = input("Enter server name: ")

        if server == "":
            print("Empty value not allowed ❌")
            continue

        if server.isdigit():
            print("Numbers not allowed ❌")
            continue

        if server in servers:
            print("Duplicate server not allowed ❌")
            continue

        servers.append(server)

    # ---------------------------
    # PRINT SERVERS
    # ---------------------------

    print("\n--- Server List ---")

    for index, server in enumerate(servers, start=1):
        print(f"{index}. {server}")

    # ---------------------------
    # SERVICE CHECK FUNCTION
    # ---------------------------

    def check_service():

        status = random.choice(["up", "down"])

        if status == "up":
            return True
        else:
            return False


    # ---------------------------
    # CHECK ALL SERVERS
    # ---------------------------

    print("\n--- Service Status ---")

    server_status = {}

    for server in servers:

        if check_service():
            print(f"{server} → UP ✅")
            server_status[server] = "UP"

        else:
            print(f"{server} → DOWN ❌")
            server_status[server] = "DOWN"


    # ---------------------------
    # WRITE LOG FILE
    # ---------------------------

    log_file = open("server.log", "a")

    log_file.write(f"\nUser: {name}\n")

    for server, status in server_status.items():
        log_file.write(f"{server} : {status}\n")

    log_file.close()

    print("\nLogs written successfully ✅")


    # ---------------------------
    # READ LOG FILE
    # ---------------------------

    print("\n--- Reading Logs ---")

    log_file = open("server.log", "r")

    content = log_file.read()

    print(content)

    log_file.close()