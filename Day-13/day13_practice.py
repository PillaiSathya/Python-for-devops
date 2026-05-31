#!/usr/bin/env python3

import subprocess
import os

user = subprocess.getoutput("whoami")
path = os.getcwd()
files = os.listdir()

print(f"Current user: {user}")
print(f"Current path: {path}")
print("\nFiles and Folders:")

for file in files:
    print(file)
