#!/usr/bin/python3
"""
loginfail = 0
keystone_file=open("/home/student/mycode/attemptlogin/keystone.common.wsgi","r")
keystone_file_lines=keystone_file.readlines()
for line in keystone_file_lines:
    if "Authorization failed" in line:
        loginfail+=1
print("The number of failed login attempts is", loginfail)
keystone_file.close
"""

"""
#!/usr/bin/python3

# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 # counter for fails

# open the file for reading
keystone_file = open("/home/student/mycode/attemptlogin/keystone.common.wsgi","r")

# loop over the file
for line in keystone_file:

    # if this 'fail pattern' appears in the line...
    if "- - - - -] Authorization failed" in line:
        loginfail += 1 # this is the same as loginfail = loginfail + 1

print("The number of failed log in attempts is", loginfail)
keystone_file.close() # close the open file
"""


# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 # counter for fails
success = 0

# open the file for reading
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:

    # loop over the file
    for line in kfile:
        # if this 'fail pattern' appears in the line...
        if "Authorization failed" in line:
            loginfail += 1 # this is the same as loginfail = loginfail + 1
            print(line.split()[-1])
        if "GET" in line or "POST" in line:
            success += 1

print("The number of failed log in attempts is", loginfail)
print("The number of successful attempts is", success)




