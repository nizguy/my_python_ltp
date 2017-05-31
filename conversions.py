def celsiusToFahrenheit(celsiusTemp):
    fahrenheit = celsiusTemp * (9.0/5.0) + 32.0
    return fahrenheit

def fahrenheitToCelsius(fahrenheitTemp):
    celsius = (fahrenheitTemp - 32.0) * (5.0/9.0)
    return celsius

def showMenu():
 print "A: Convert celsius to fahrenheit"
 print "B: Convert fahrenheit to celsius"

def showMenu2():
 print "A: Convert celsius to fahrenheit"
 print "B: Convert fahrenheit to celsius"
 print "Any other option will put you into a loop"

showMenu()
option = raw_input("Option: ")

showMenu2()
option = raw_input("Pick Option A or B: ")

import time

while option != "X":
    if option == "A" or option == "B" or option == "a" or option == "b" :
        value = input("Number to convert: ")
        if option == "A":
            print (celsiusToFahrenheit(float(value)))
        elif option == "B":
            print (fahrenheitToCelsius(float(value)))

    else:
           print "Lets try again J.L. "
           time.sleep(2.1)    # pause 2.1 seconds
           print "This time enter a valid option case sensitive (A or B) dipshit! "
    showMenu2()
    option = raw_input("Option: ")
