#!/usr/bin/env python3
def server_status(server, status):
    print (f"Server {server} is {status}")
server = input("Enter server name: ")
status = input("Enter server status: ")
server_status(server, status)
