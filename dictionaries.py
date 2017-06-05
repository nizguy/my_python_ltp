gpas = {
        "Mark Lassoff" : 3.45,
        "Fred Smith" : 2.99,
        "Mary Johnson" : 2.55,
        "John Johnson" : 1.95,
        "Louis Lane" : 3.15,
        "Brett Smith" : 4.0,
        
    }

print "The GPA is: ", (gpas["Mark Lassoff"])
print "The GPA is: ", (gpas["Brett Smith"])

gpas["Louis Lane"] = 2.75

gpas["Thomas Smith"] = 2.61
del gpas["Fred Smith"]

# To test if a key is in the data use .has_key

if gpas.has_key("Mark Lassoff"):
    print "Mark is entered"

# test for a key that doesn't exist use .has_key  with "else"

if gpas.has_key("Fred Smith"):
    print "Fed is entered"
else:
    print "Fred has escaped"

print gpas.keys()
print gpas.values()

print len(gpas)
