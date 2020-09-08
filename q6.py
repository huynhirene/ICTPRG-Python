# Write a program that can output the following shape to the console:
# xxxxx
# xxxxx
# xxxxx
# xxxxx
# xxxxx
# Please ensure that you only have the following print statements within your application:
# print("x", end='')
# print("")
# You will need to use two loops for this to work.

rows = 5
lines = 0

for x in range(0,rows):
    for x in range(lines,rows):
        print("x", end="")
    print("")
    
