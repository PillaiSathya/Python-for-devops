#!/usr/bin/env python3

log_file = open("server.log", "a")

log_file.write("Server started successfully\n")
log_file.write("Nginx service running\n")
log_file.write("[INFO] Docker started\n")

log_file.close()

print("logs written successfully ✅ ")

