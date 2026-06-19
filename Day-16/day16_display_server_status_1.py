#!/usr/bin/env python3

def deploy_servers(servers):
    for server in servers:
        print(f"Deploying application to {server}")

server_list = ["web1", "web2", "web3"]
deploy_servers(server_list)
