#!/usr/bin/env python3

import sys

if len(sys.argv) < 3:
    print("Usage : ./day14_deploy.py <enviroment> <service>")
else:
    enviroment = sys.argv[1]
    service = sys.argv[2]

    print(f"Environment: {enviroment}")
    print(f"Service: {service}")
    print(f"Deploying {service} to {enviroment}🚀🚀")
