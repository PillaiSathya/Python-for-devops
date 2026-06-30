1. What is a service?
A. Service is a program that runs in the background. Unlike normal programs, services are designed to keep running
   until they are stopped or the system shuts down. eg.web server - nginx, Docker - docker, SSH server - sshd, Scheduler -cron  

2. What is systemd?
A. It is a service manager. It is responsible for start, stop, monitor and managing dependencies between services. It also starts service automatically during system boot.

3. Boot process
A. Power ON
      ↓
   Bootloader
      ↓
   Linux Kernel
      ↓
   systemd (PID 1)
      ↓
   Starts Services
      ↓
   Login Screen /Terminal

4. Why PID 1?
A. systemd is the first userspace process started by Linux kernel and is assigned PID 1. The kernel itself runs first. Then it starts systemd.

5. systemctl
A. systemctl is the command used to communicate with systemd
  You
   ↓
  systemctl
   ↓
  systemd
   ↓
  Service 

6. start
A. start the service

7. stop
A. Stops the service

8. restart
A. stops the service and starts it again

9. reload
A. Reloads the configuration without fully stopping the service, if service supports it.

10. enable
A.  enable a service to start automatically whenever the system boots.

11. disable
A.  disable the service at boot 

12. one real-world example.

Suppose you modify:
/etc/nginx/nginx.conf
Now you have two choices.

Restart
sudo systemctl restart nginx
Result:
Stop nginx
↓
Start nginx
Users may briefly lose connections.

Reload
sudo systemctl reload nginx
Result:
Reload configuration
↓
No downtime
This is why production engineers often prefer reload when possible.

13. Commands:
systemctl status nginx ---> check the status of the nginx
systemctl list-units --type=service --state=running  ---> list running services
systemctl status ---> check system status
sudo systemctl start nginx ---> start a service
sudo systemctl stop nginx ---> stop a service
sudo systemctl restart nginx ---> restart a service
sudo systemctl reload nginx ---> reload configuration without stopping the service
sudo systemctl enable nginx ---> Enable service at boot
sudo systemctl disable nginx ---> disable automatic startup
sudo systemctl is-active nginx ---> to check active or inactive
