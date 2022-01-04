import random                    #Importing modules random to get some functions
roll = random.randint(1,6)
                              #print("The Computer rolled a " + str(roll))
guess = int(input("Guess the dice roll:\n"))

if guess == roll:
    print("Correct they rolled a " + str(roll))
else: 
    print("Wrong They rolled a " + str(roll))