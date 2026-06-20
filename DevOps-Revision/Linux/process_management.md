# Linux Process Management

## What is a Process?

A process is a program that is currently running in memory.

Examples:

* nginx
* bash
* python
* systemd

---

## What is PID?

PID stands for Process ID.

Every running process in Linux is assigned a unique PID.

Example:

```bash
PID 1     -> systemd
PID 328   -> bash
```

---

## Process Commands

### ps

Shows running processes.

```bash
ps
```

Example Output:

```bash
PID TTY          TIME CMD
328 pts/0    00:00:00 bash
1735 pts/0   00:00:00 ps
```

---

### ps -ef

Shows detailed information about all running processes.

```bash
ps -ef
```

Important Fields:

* UID  -> User ID
* PID  -> Process ID
* PPID -> Parent Process ID
* CMD  -> Command

---

### pgrep

Find process by name.

```bash
pgrep bash
```

Output:

```bash
328
637
1330
```

Returns Process IDs (PIDs).

---

### top

Displays real-time process and system information.

```bash
top
```

Shows:

* CPU Usage
* Memory Usage
* Running Processes
* Load Average

Example:

```text
Tasks: 75 total, 1 running, 74 sleeping, 0 zombie
```

Meaning:

* 75 processes exist
* 1 process running
* 74 processes sleeping
* 0 zombie processes

---

## Stopping Processes

### kill

Gracefully stops a process.

```bash
kill PID
```

Example:

```bash
kill 1234
```

---

### kill -9

Forcefully terminates a process.

```bash
kill -9 PID
```

Example:

```bash
kill -9 1234
```

---

## Important Interview Points

### What is a Process?

A program currently running in memory.

### What is PID?

Process ID. A unique identifier assigned to a running process.

### Process vs Program

Program:
A file stored on disk.

Example:
python app.py

Process:
A running instance of a program in memory.

### Which command shows running processes?

```bash
ps
```

### Which command shows detailed process information?

```bash
ps -ef
```

### Which command finds a process by name?

```bash
pgrep <process_name>
```

### Difference between kill and kill -9

kill:

* Gracefully stops a process

kill -9:

* Forcefully terminates a process

### What is PID 1?

Usually:

```bash
systemd
```

The first process started during system boot.

