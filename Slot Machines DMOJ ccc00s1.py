# Slot Machines DMOJ ccc00s1

# Canadian Computing Competition: 2000 Stage 1, Junior #3, Senior #1

# Martha takes a jar of quarters to the casino with the intention of becoming rich. She plays three machines in turn. 
# Unknown to her, the machines are entirely predictable. Each play costs one quarter. 
# The first machine pays 30 quarters every 35 t h time it is played; 
# the second machine pays 60 quarters every 100 t h time it is played; the third pays 9 quarters every 10 t h time it is played.
# Input Specification

# Your program should take as input the number of quarters in Martha's jar (there will be at least one and fewer than 1000 ), 
# and the number of times each machine has been played since it last paid.
# Output Specification

# Your program should output the number of times Martha plays until she goes broke.

while True:
    quarters = int(input())
    if (1 <= quarters < 1000):
        break
    else:
        print("Please enter the number of quarters (1-999)")

while True:
    m1 = int(input())
    if (0 <= m1 <= 34):
        break
    else:
        print("Please enter the number of plays since the 1st machine has paid out (0-34)")

while True:
    m2 = int(input())
    if (0 <= m2 <= 99):
        break
    else:
        print("Please enter the number of plays since the 1st machine has paid out (0-99)")

while True:
    m3 = int(input())
    if (0 <= m3 <= 9):
        break
    else:
        print("Please enter the number of plays since the 1st machine has paid out (0-9)")

# Initialize number of plays
plays = 0

# Start loop
while quarters > 0:
    m1 += 1
    quarters -= 1
    plays += 1
    if quarters == 0:
        break
    if m1 == 35:
        quarters += 30
        m1 = 0
        #print(f"Machine 1 has paid out!")
    #print(f"The number of plays is: {plays}")
    #print(f"The number of quarters is: {quarters}")
    #print(f"Machine 1 pays out in {(35 - m1)} plays")
    m2 += 1
    quarters -= 1
    plays += 1
    if quarters == 0:
        break
    if m2 == 100:
        quarters += 60
        m2 = 0
        #print(f"Machine 2 has paid out!")
    #print(f"The number of plays is: {plays}")
    #print(f"The number of quarters is: {quarters}")
    #print(f"Machine 2 pays out in {(100 - m2)} plays")
    m3 += 1
    quarters -= 1
    plays += 1
    if quarters == 0:
        break
    if m3 == 10:
        quarters += 9
        m3 = 0
        #print(f"Machine 3 has paid out!")
    #print(f"Machine 3 pays out in {(10 - m3)} plays")
    #print(f"The number of plays is: {plays}")
    #print(f"The number of quarters is: {quarters}")
#
print(f"Martha plays {plays} times before going broke.")