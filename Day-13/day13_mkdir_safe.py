#!/usr/bin/env python3

import os

try:
    os.mkdir("backup")
    print("Folder created successfully")

except FileExistsError:
    print("Folder already exist ⚠️")
        
