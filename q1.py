# Write a program that counts from 0 to 25, outputting each number on a new line.

num = 0

while num <= 26:
    print(num)
    num = num + 1 
    if num == 26:
        break

# OR

for numbers in range(0,26):
    print(numbers)