#!/usr/bin/env python3

import sys

def deploy(environment, service):
    print(f"Deploying {service} to {environment}")

deploy(sys.argv[1], sys.argv[2])

