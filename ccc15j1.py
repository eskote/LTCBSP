# ccc15j1

PN = str(input()) # Takes phone number as input and strips leading or trailing whitespace
PN = ''.join(PN.split()) # removes any whitespace inside the string  
# verify that exactly 9 digits were entered
if PN.isdigit() and len(PN) == 10 and PN.startswith(str(437)) or PN.startswith(str(416)) or PN.startswith(str(647)):
    if PN.startswith(str(416)):
        print("valuable")
    else:
        print("valueless")
else:
    print("invalid")

