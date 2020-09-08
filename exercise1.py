# Write a loop that lets the user enter a number 
# The number should be multiplied by 10 and the result will be assigned to a variable named "prod"
# The loops should iterate as long as the product is less than 100


# THIS IS AN EXAMPLE OF HOW A WHILE LOOP IS BETTER THAN A FOR LOOP 

while True:
    number = int(input("Enter a number: "))
    prod = number * 10 
    print(prod)
    if prod >= 100:
        break
print("Exit.")

