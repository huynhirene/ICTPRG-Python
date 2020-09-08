# Write a program that could be used for an (unsecure) login, with a username and password. For example:
# -------------------------------------
# Enter username: bob
# Enter password: password1234
# Access Granted!
# -------------------------------------
# Enter username: frank
# Enter password: invalidpass
# Access Denied!
# -------------------------------------
# (Reference your algorithm from the 'Introduction to Algorithms' Quiz)

username = str(input("Enter username: "))
password = str(input("Enter password: "))

if username == "bob" and password == "password1234":
    print("Access granted!")
else:
    print("Access denied.")

