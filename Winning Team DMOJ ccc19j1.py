# Winning Team DMOJ ccc19j1
# Canadian Computing Competition: 2019 Stage 1, Junior #1

# You record all of the scoring activity at a basketball game. Points are scored by a 3 -point shot, a 2 -point field goal, or a 1 -point free throw.

# You know the number of each of these types of scoring for the two teams: the Apples and the Bananas. 
# Your job is to determine which team won, or if the game ended in a tie.

# Input Specification

# The first three lines of input describe the scoring of the Apples, and the next three lines of input describe the scoring of the Bananas. 
# For each team, the first line contains the number of successful 3 -point shots, the second line contains the number of successful 2 -point field goals, 
# and the third line contains the number of successful 1 -point free throws. Each number will be an integer between 0 and 100 , inclusive.

# Output Specification

# The output will be a single character. If the Apples scored more points than the Bananas, output A. If the Bananas scored more points than the Apples, output B. 
# Otherwise, output T, to indicate a tie.

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
    