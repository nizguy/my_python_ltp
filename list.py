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

for score in gpas:
  print score

total = 0
for score in gpas:
    total = total + score
print "The original average GPA is ", (total/5)

gpas.append(1.55)

total = 0
for score in gpas:
    total = total + score
print "The the current average GPA is ", (total/len(gpas))

