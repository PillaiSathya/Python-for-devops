#!/usr/bin/env python3

def deploy(environment = "production"):
    print(f"Deploying to {environment}")

deploy()
deploy("staging")

