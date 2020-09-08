# Write a program that asks the user for their year of birth, 
# checks if they are of legal drinking age, and tells the user to come into the bar. 
# Example:
# What is your Year of birth: 1995
# You are: 25 Years old
# Come in and have a drink!
 
# What is your Year of birth: 2003
# You are: 17 Years old
# Go away. Child.	


asking_age = int(input("What year were you born? "))
current_year = int("2020") 
drinker_age = current_year - asking_age
print("You are:", (current_year - asking_age))


if drinker_age >= 21:
    print("Come in and have a drink!")
else:
    print("You are a child. Go away!")


