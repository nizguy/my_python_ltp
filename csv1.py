import csv

sports = open("sports.csv", "r")
try:
    reader = csv.reader(sports)
    for row in reader:
        print "\n"
        for item in row:
            print item
    print "\n"
    
finally:
    sports.close
