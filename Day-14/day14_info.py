#!/usr/bin/env python3

import sys

if len(sys.argv) < 3:
    print("Usage: ./day14_info.py <Sathya> <Docker>")
else:
    Sathya = sys.argv[1]
    Docker = sys.argv[2]

    print(f"Name: {Sathya}")
    print(f"Course: {Docker}")
    print(f"Welcome {Sathya} to {Docker}🚀")
