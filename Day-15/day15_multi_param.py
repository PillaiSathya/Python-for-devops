#!/usr/bin/env python3

def deploy(environment, service):
    print(f"Deploying {service} to {environment}")

deploy("production", "nginx")
deploy("staging", "docker")
deploy("dev", "kubernetes")


