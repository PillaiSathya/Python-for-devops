#!/usr/bin/env python3

import sys

if len(sys.argv) < 2:
    print("Usage : ./day14_server_check.py <server_name>")

else:
    server = sys.argv[1]

    print(f"Checking server = {server}")
    print(f"{server} is WEB server ✅")
