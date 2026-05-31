#!/usr/bin/env python3

import subprocess
output = subprocess.getoutput("whoami")
print(output)
