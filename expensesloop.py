#Acronyms = ["LOL", "IDK", "SMH", "GTFO"]
#Acronyms.append ("WTF")
#Acronyms.remove ("LOL")

#Print List in a seperate line use For(Loop)
#Syntax of a For Loop
#for-variable-in-list
#For acronym in acronyms:
#Print(acronym)


#expenses = [10.50, 8, 5, 15, 20, 5, 3] The shorter version of loop
#total = sum(expenses)
#print("You spent $", total, " on lunch this week.", sep="")

#sum = 0 The long way aka For Loop
#for x in expenses:
    #sum = sum + x

#print("you spent $", sum, " on lunch this week", sep='')

#total = 0 
#expenses = []
#for i in range(7):
    #expenses.append(float(input("Enter an expense:")))

#total = sum(expenses)

#print ("You spent $", total, sep='')

total = 0
expenses = []
num_expenses = int(input("Enter # of expenses:"))
for i in range(num_expenses):
    expenses.append(float(input("Enter an expense:")))
total = sum(expenses)
print("You spent $", total, sep='') 