#!/usr/bin/env python3

import os
current_path = os.getcwd()
print(f"Current directory : {current_path}")
print(f"Files and Folder:")
files = os.listdir()
for file in files:
    print(file)

