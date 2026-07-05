#!/usr/bin/env python3

ports = {
    "nginx": 80,
    "ssh": 22,
    "docker": 2375,
    "kubernetes": 6443
 }

service = input("Enter service: ")

port = ports.get(service, "service not found")

print("Port:", port)


