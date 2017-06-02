names = ["Mark" , "Fred" , "Tom" , "Wendy" , "Kevin" ]
gpas = [ 3.41, 2.55, 4.0, 2.95, 3.75 ]

print names[0]
print names[3]

print gpas[0]
names.append("Brett")
print names[5]
del names[5]

for name in names:
    print name

gpas.append(1.55)

total = 0
for score in gpas:
    total = total + score
print "The average GPA is ", (total/len(gpas))
