# Write a program that asks the user for their name, 
# checks if their name is either "frank" or "george" and if it is, greet them by their name.
# (Reference your algorithm from the 'Introduction to Algorithms' Quiz)

name_user = input("Enter your name: ")

if name_user == "frank" or name_user == "george":
    print("Hello, how are you? " + name_user) 
else:
    print("Do I know you?")

