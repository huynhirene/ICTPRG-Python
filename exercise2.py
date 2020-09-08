# Design a repitition loop that asks for the number of times a loop should run 
# In the loop, a number will be entered and 
# a running total of the numbers entered in each iteration of the loop will be calculated 
# This total will be printed once you exit the loop 

loop_run = input("How many times should the loop run? ")

while True:
    num = input("Enter numbers: ")
    num = num + loop_run
    if num == loop_run:
        print(num)
        



    

  

