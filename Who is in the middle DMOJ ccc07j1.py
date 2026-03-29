# Who is in the middle DMOJ ccc07j1

# Canadian Computing Competition: 2007 Stage 1, Junior #1

# In the story Goldilocks and the Three Bears, each bear had a bowl of porridge to eat while sitting at his/her favourite chair. 
# What the story didn't tell us is that Goldilocks moved the bowls around on the table, so the bowls were not at the right seats anymore. 
# The bowls can be sorted by weight with the lightest bowl being the Baby Bear's bowl, 
# the medium bowl being the Mama Bear's bowl and the heaviest bowl being the Papa Bear's bowl.

# Write a program that reads in three weights and prints out the weight of Mama Bear's bowl. 
# You may assume all weights are positive integers less than 100.

while True:
    W1 = int(input())
    if (0 < W1 <101):
        break
    else: 
        print("Please enter a weight between 1-100.")

while True:
    W2 = int(input())
    if (0 < W2 <101):
        break
    else: 
        print("Please enter a weight between 1-100.")

while True:
    W3 = int(input())
    if (0 < W3 <101):
        break
    else: 
        print("Please enter a weight between 1-100.")

bowls = [W1, W2, W3]
sorted_bowls = sorted(bowls)

result = [sorted_bowls[2], sorted_bowls[1], sorted_bowls[0]]

print(sorted_bowls[1])