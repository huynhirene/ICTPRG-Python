# Copy and Modify Question 3, to support the following username password combinations:
# bob : password1234
# fred : happyPass122
# lock: passwithlock44
# Please ensure that the password only works with the corresponding username.

username = str(input("Enter username: "))
password = str(input("Enter password: "))

if username == "bob" and password == "password1234":
    print("Access granted!")
elif username == "fred" and password == "happyPass122":
    print("Access granted!")
elif username == "lock" and password == "passwithlock44":
    print("Access granted!")
else:
    print("Access denied.")



