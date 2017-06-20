import re

phoneNumber = "1-800-555-1960 #This is my phone number"

phoneNumberClean = re.sub(r'#.*$', "Mark Burns", phoneNumber)
print phoneNumberClean

num = re.sub(r'\D', "", phoneNumber)
print num
