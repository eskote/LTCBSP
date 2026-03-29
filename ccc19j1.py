# ccc19j1

# Input Points for Apples
while True:
    A3 = int(input()) # Number of 3 point shots for Apples
    if (0 <= A3 <= 100):
        break
    else: print("Please enter the number of 3 point shots for Apples between 0-100.")
while True:
    A2 = int(input()) # Number of 2 point field goals for Apples
    if (0 <= A2 <= 100):
        break
    else: print("Please enter the number of 2 point shots for Apples between 0-100.")
while True:
    A1 = int(input()) # Number of free throws for Apples
    if (0 <= A1 <= 100):
        break
    else: print("Please enter the number of 1 point shots for Apples between 0-100.")

# Total points for Apples
ATP = ((A3 * 3) + (A2 * 2) + (A1 * 1))

# Input points for Bananas
while True:
    B3 = int(input()) # Number of 3 point shots for Apples
    if (0 <= B3 <= 100):
        break
    else: print("Please enter the number of 3 point shots for Bananas between 0-100.")
while True:
    B2 = int(input()) # Number of 2 point field goals for Apples
    if (0 <= B2 <= 100):
        break
    else: print("Please enter the number of 2 point shots for Bananas between 0-100.")
while True:
    B1 = int(input()) # Number of free throws for Apples
    if (0 <= B1 <= 100):
        break
    else: print("Please enter the number of 1 point shots for Bananas between 0-100.")

# Total number of points for Bananas
BTP = ((B3 * 3) + (B2 * 2) + (B1 * 1)) 

if (ATP > BTP):
    print("A")
elif (BTP > ATP):
    print("B")
else:
    print("T")
    