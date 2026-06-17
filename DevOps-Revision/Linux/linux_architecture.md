1. What is Linux?
A: Linux is a open-source Operating System based on the Linux kernel.
It is widely used in servers, cloud environments,containers and Devops platforms.
Popular distributions include Ubuntu, Red Hat Enterprise Linux, CentOS, Debian and Amazon Linux.


2. What is Kernel?
A: Kernel is the core component of Linux.
It acts as a bridge between applications and Hardware.
It manages:
- CPU
- Memory
- Devices
- Processes
- Filesystems

3. What is Shell?
A: Shell is a command line interpreter.
like:-  sathya@DESKTOP-0H7NLRA:~$ ls
It accepts commands from users and passes them to kernel for execution.
eg. bash, sh, zsh are shell programs(command interpreters)

user-->shell-->kernel

The shell is like a translator. 
The shell acts as an interface between the user and the kernel

4. Explian the flow:Linux Architecture
User --> Shell --> Kernel --> Hardware
A: 
You
 ↓
Shell receives "ls"
 ↓
Shell asks Kernel
 ↓
Kernel accesses filesystem
 ↓
Hardware provides data
 ↓
Kernel returns result
 ↓
Shell displays output

5. Difference between Kernel and Shell?
A: 
| Kernel               | Shell               |
| -------------------- | ------------------- |
| Core of OS           | Interface for users |
| Manages hardware     | Accepts commands    |
| Runs in kernel space | Runs in user space  |
| Talks to hardware    | Talks to kernel     |


6. What is the purpose of :
/etc
/home
/var
/usr
/tmp
A:
/etc : Configuration files /etc/passwd or /etc/hosts /etc/fstab 
       Stores system configuration files
/home : personal folders, user files eg. /home/sathya
/var : Variable data /var/log, /var/cache Logs and changing data
/usr : Installed prgms and binaries eg /usr/bin, /usr/local/bin applications
/tmp : temporaty files used by applications during execution.
