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

user = str(input("Enter username: "))
password1 = str(input("Enter password: "))

if user == "bob":
    print("Welcome back " + user)
    if password1 == "password1234":
        print("You have entered the correct password.")
        print("Access granted!")
    else:
        print("You have entered the incorrect password.")
        print("Access denied.")
else:
    print("Incorrect user. Would you like to make a new account?")