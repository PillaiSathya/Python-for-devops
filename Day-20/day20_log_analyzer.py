#!/usr/bin/env python3 

def show_logs(content):
    with open("application.log","w")as file:
        for line in content:
            file.write(line + "\n")

log_content = [
    "INFO: Application Started",
    "ERROR: Database Connection Failed",
    "INFO: User Logged In",
    "ERROR: Disk Full",
    "INFO: Backup Completed"
]

show_logs(log_content)

def count_errors(content):
    count = 0
    for line in content:
        if "ERROR" in line:
            count += 1
    return count

total = count_errors(log_content)
print(f"Total Errors: {total}")
