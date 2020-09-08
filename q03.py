# Write a program that keeps asking a user for a number, until the number is within the range of 50 and 70. Example:
# Enter a number: 42
# Not within range.
# Enter a number:53
# Within range.

numbers = 0

for i in range(50,70):
    numbers = int(input("Enter a number: "))
    if numbers < 50 and numbers > 70:
        print("Not within range.")
    else:
        print("Within range.")