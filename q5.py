# Write a program that can grade a student based upon a percentage grade. Example:
# What was your grade: 99
# You will receive a "High Distinction"
# Please use the following grade table within your application:
# High Distinction	100 - 90
# Distinction	89- 80
# Credit	79 - 70
# Pass	69 - 50

grade = int(input("What was your grade? "))

if grade >= 90:
    print("You will receive a 'High Distinction'")
elif grade >=80:
    print("You will receive a 'Distinction'")
elif grade >= 70:
    print("You will recive a 'Credit'")
elif grade >=50:
    print("You will receive a 'Pass'")
else:
    print("You have failed. Please speak to teacher.")


