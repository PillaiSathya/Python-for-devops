#!/usr/bin/env python3

import random

# ---------------------------
# USER DETAILS
# ---------------------------

name = input("Enter user name: ")
role = input("Enter the role: ")

print(f"\nHello {name}, welcome {role}🚀🚀" )

# ---------------------------
# LOGIN SYSTEM
# ---------------------------

correct_password = "admin123"
attempts = 0
max_attempts = 3
logged_in = False

while attempts < max_attempts:
    
    password = input("\n Enter the password: ")

    if password == correct_password:
        print(f"\nLogged in successfully✅")
        logged_in = True
        break

    else:
        print(f"\nWrong Password❌")
        print(f"attempts left : {max_attempts - attempts - 1}")

    attempts += 1

# ---------------------------
# LoGIN FAILED
# ---------------------------

if not logged_in:
    print(f"\n Accont Locked🔒 ")

else:

    # ---------------------------
    # SERVER LIST
    # ---------------------------

    servers = []

    while len(servers) < 3:

        server = input("Enter the server name: ")

        if server == "":
            print(f"\n Empty string is not allowed")
            continue
            
        if server.isdigit():
            print(f"\n Numbers not allowed")
            continue
            
        if server in servers:
            print(f"\n Duplicate servers not allowed")
            continue
            
        servers.append(server)

    # ---------------------------
    # PRINT SERVERS
    # ---------------------------           
    
    print("\n ----------Server List----------")

    for index, server in enumerate (servers, start=1):
        print(f"\n {index}. {server}")

    # ---------------------------
    # SERVICE CHECK FUNCTION
    # ---------------------------

    def check_service():
        status=random.choice(["up","down"])
        if server == "up":
            return True
        else:
            return False


    # ---------------------------
    # CHECK ALL SERVERS
    # ---------------------------    
    
    print("\n-------- SERVICE CHECK -------------")    

    server_status = {}
    for server in servers:
        if check_service():
            print(f"{server} : UP")
            server_status [server] = "UP"
        else:
            print(f"{server} : DOWN")
            server_status [server] = "Down"

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
