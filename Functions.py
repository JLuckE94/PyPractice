#Reasons to use function- Reuse chunk of code over n over, Organize your code by logical units

#Global way not good becomes messy
#def greeting():
    #print("Hello", name)

#name = input("enter your name:\n")
#greeting()
#name2 = input("enter another name:\n")
#name = name2
#greeting()

#Local Scope Function EX:

def greeting(name):
    print("Hello", name)

name1 = input("Enter your name:\n")
greeting(name1)
name2 = input("Enter another name:\n")
greeting(name2) 

def addition( a, b): #4- Addition function
    return a + b #5
#Main Program
num1 = float(input("Enter your 1st number:\n")) #First step
num2 = float(input("Enter your 2nd number:\n")) #second step
result = addition(num1, num2) #3rd
print("The result is", result)#6

#Organized version must indent code underneath function
def main():
    num1 = float(input("Enter your 1st number:\n")) #First step
    num2 = float(input("Enter your 2nd number:\n")) #second step
    result = addition(num1, num2) #3rd
    print("The result is", result)#6
main()#How to print function