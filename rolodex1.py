#!/usr/local/bin/python2.7

import csv

print "Welcome To My Rolodex"
print "Please Use The Following Menu To Enter New Contacts: "


def menu():
    print "To Add to Rolodex - Enter N"
    print "View List of Contacts - Enter V"
    print "To Quite Program - Enter Q"
    selection = raw_input("Shall We begin? =>")
    if selection == "N":
        addToRolodex()
    elif selection == "V":
        viewRolodex()
    elif selection == "Q":
        quit()
    else:
        print "Shall We Try Again?"
    menu()

def addToRolodex():
    print "Enter New Contact"
    firstName = raw_input("First Name:")
    lastName = raw_input("Last Name:")
    email = raw_input("Email:")
    phone = raw_input("Phone:")
    directory = open("contacts.csv", "a")
    outstring = firstName + "," + lastName + "," + email + "," + phone + "\n"
    directory.write(outstring)
    directory.close()
    print (firstName + " " + lastName + " Added To Rolodex.")
    menu()

def viewRolodex():
    print "View Contacts"
    directory = open("contacts.csv", "r")
    try:
        rowtext = ""
        reader = csv.reader(directory)
        for row in reader:
            for item in row:
                rowtext = rowtext + " " + item
            print rowtext
            rowtext = ""
    finally:
            directory.close()
    menu()
menu()

    

    
