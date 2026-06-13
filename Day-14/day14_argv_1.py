#!/usr/bin/env python3

import sys

if len(sys.argv) < 2:
    print("Usage: ./day14_check.py <server_name>")

else:
    server = sys.argv[1]

    print(f"Checking server = {server}")

    if server == "db1":
        print(f"{server} is DATABASE server ✅ ")
    elif server == "web1":
        print(f"{server} is WEB based server ✅ ")
    else:
        print(f"{server} is UNKNOWN server⚠️ ")
