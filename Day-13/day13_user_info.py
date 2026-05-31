#!/usr/bin/env python3

import subprocess

user = subprocess.getoutput("whoami")
path = subprocess.getoutput("pwd")

print(f"Current user: {user}")
print(f"Current path: {path}")

