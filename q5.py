# Write a program that keeps asking the user for a number, and adds it to a total. Ensure that pressing x stops entering numbers. Example:
# Enter some numbers (Press x to stop):
# 1
# 3
# 66
# x
# Total: 70

# Input numbers 
# If numbers don't equal x continue 
# If numbers equal x  
# Print totals 


numbers = 0
total_numbers = 0

while numbers != "x":
    numbers = input("Enter some numbers (Press x to stop): ")
    if numbers != "x":
        total_numbers = total_numbers + int(numbers)
    else:
        print("Total numbers: " + str(total_numbers))
    
        

