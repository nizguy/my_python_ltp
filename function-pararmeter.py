def greetPerson(name):
    "This function greets the user by name"
    print "Greetings", name
   
personName = raw_input("What is your name? ")
greetPerson(personName)

def addThese(a,b):
    "Adds two numbers together"
    c = a + b
    print c

addThese(234, 17)

family = ["Debbie" , "Mark" , "Cecil" , "David" , "Ivy"]

def printFirst(myList):
    print myList[0]

printFirst(family)
