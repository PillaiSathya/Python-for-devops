Let's go line by line.

#!/usr/bin/env python3
What is this?

Called a shebang.

It tells Linux:

"Run this file using Python3."

When you execute:

./day18_write_log.py

Linux reads:

#!/usr/bin/env python3

and understands:

python3 day18_write_log.py
Line 2
def write_log(message):
What is happening?

Creating a function named:

write_log

The word inside brackets:

message

is called a parameter.

Think of it like an empty box waiting for a value.

Example:

write_log("web1 is UP")

Now Python does:

message = "web1 is UP"
Line 3
with open("server.log", "a") as file:

This is one of Python's built-in file handling features.

open()

Built-in function.

Used to open a file.

General syntax:

open(filename, mode)

Example:

open("server.log", "a")

means:

Open server.log
in append mode
What does with do?

Before modern Python, people wrote:

file = open("server.log", "a")

file.write("hello")

file.close()

Problem:

If program crashes,

file.close()

may never run.

File remains open.

Bad practice.

Modern way:

with open("server.log", "a") as file:

Python automatically:

Open file
Do work
Close file

No need:

file.close()

This is why DevOps engineers usually use:

with open(...)
What is "a"?

Mode.

Read
"r"

Read only.

Example:

with open("server.log", "r") as file:
Write
"w"

Creates file or overwrites everything.

Example:

Current file:

web1
web2

Run:

with open("server.log","w")

Write:

db1

Result:

db1

Old content gone.

Append
"a"

Adds at the end.

Current file:

web1
web2

Append:

db1

Result:

web1
web2
db1

Nothing deleted.

What is as file?
with open("server.log", "a") as file:

Python opens file and stores it in variable:

file

Think:

file = opened server.log

Now you can use:

file.write(...)
Next Line
file.write(message + "\n")
What is message?

Remember:

def write_log(message):

Message is parameter.

When you call:

write_log("web1 is UP")

Python internally does:

message = "web1 is UP"

Then:

file.write(message + "\n")

becomes:

file.write("web1 is UP\n")
What is \n?

New line.

Without:

file.write("web1")
file.write("db1")

Result:

web1db1

With:

file.write("web1\n")
file.write("db1\n")

Result:

web1
db1
Function Calls
write_log("web1 is UP")

Python does:

message = "web1 is UP"

and writes:

web1 is UP

to file.

Next:

write_log("db1 is DOWN")

Python does:

message = "db1 is DOWN"

and writes:

db1 is DOWN

to file.

Reading File

Now compare:

Write
def write_log(message):

    with open("server.log", "a") as file:
        file.write(message + "\n")
Read
def read_log():

    with open("server.log", "r") as file:
        content = file.read()

    print(content)
Difference
Writing

We SEND data TO file.

file.write(...)

Direction:

Python ---> File
Reading

We GET data FROM file.

content = file.read()

Direction:

File ---> Python
Why no message parameter in read?

Writing needs data:

write_log("web1 is UP")

because Python needs to know what to write.

Reading doesn't need data.

It simply says:

Read everything from file

So:

def read_log():

has no parameter.

One last observation

You noticed:

web1 is UP
db1 is DOWN
web1 is UP
db1 is DOWN
web is UP
db1 is DOWN

Why duplicates?

Because every time you run:

with open("server.log", "a")

append mode adds new lines to the existing file.

Nothing gets removed.

That's exactly how log files work in Linux and DevOps.

This Day 18 lesson is actually very important because Jenkins logs, application logs, Kubernetes logs, and audit logs all work using the same write/read concepts you're learning now. 🚀
