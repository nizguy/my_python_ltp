studentGpasDictionary1 = {}

print "Enter Students Name and correct GPA"
print "(Press x to quit & get High/Low & Median GPAS)"

studentName = raw_input("Enter Students Name :")
if studentName != "x":
       studentGpa = raw_input("Enter Students GPA : ")
while studentName != "x":
    studentGpasDictionary1[studentName] = studentGpa
    studentName = raw_input("Student Name :")
    if studentName != "x":
        studentGpa = raw_input("Student GPA : ")

highest = 0.0
lowest = 4.0
print "Class GPA List"
for key,value in studentGpasDictionary1.items():
    print key, ":", value
    if value  > highest:
        highest = value
    if value < lowest:
        lowest = value
aGpa = studentGpasDictionary1.values()
totalGPA=0

print "Average GPA: ", (totalGPA/len(aGpa))
print "Highest GPA: ", highest
print "Lowest GPA: ", lowest
print "Median GPA: ", numpy.median(aGpa)

aGpa = studentGpasDictionary1.values()
totalGPA=0

for avgerage in aGpa:
    totalGPA = totalGPA + avgerage

