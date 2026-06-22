
1. what is UID?
A. Unique ID assigned to user

2. What is GID?
A. Unique ID assigned to group

3. whoami
A. Displays the currently logged-in user.

4. id
A. Displays user and group information for the current user.
    Example:
    uid=1000(sathya) gid=1000(sathya) groups=1000(sathya),27(sudo),1001(docker)

5. groups
A. whcih groups your user belongs to
    Linux permissions are often granted to groups rather than individual users.

6. chmod
A. Changes permission
   eg. chmod 755 script.sh
    Owner  = 7 = rwx
    Group  = 5 = r-x
    Others = 5 = r-x

7. chown
A. changes file ownership.
    sudo chown sathya file.txt
 
8. Permission Structure
    -rw-r--r--
A.  - rw- r-- r--
      |   |   |
    Owner Group Others
Owner:

rwx

✅ Read
✅ Write
✅ Execute

Group:

r-x

✅ Read
❌ Write
✅ Execute

Others:
r--

✅ Read
❌ Write
❌ Execute

9. Difference between chmod and chown?
A. chmod changes the permission rights like read write execute for the file.
    chown changes the ownership for the file. 
