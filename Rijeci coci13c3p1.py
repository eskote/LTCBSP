# Rijeci coci13c3p1

# One day, little Mirko came across a funny looking machine! 
# It consisted of a very very large screen and a single button. 
# When he found the machine, the screen displayed only the letter A. 
# After he pressed the button, the letter changed to B. 
# The next few times he pressed the button, the word transformed from B to BA, then to BAB, then to BABBA. 
# When he saw this, Mirko realized that the machine alters the word in a way 
# that all the letters B get transformed to BA and all the letters A get transformed to B.

# Amused by the machine, Mirko asked you a very difficult question! 
# After K times of pressing the button, how much letters A and how much letters B will be displayed on the screen?
# Input Specification

# The first line of input contains the integer K ( 1 ≤ K ≤ 45 ) , the number of times Mirko pressed the button.
# Output Specification

# The first and only line of output must contain two space-separated integers, the number of letters A and the number of letters B.
# Scoring

# In test data worth 20 % of total points, K will be less or equal to 10 .

while True:
    K = int(input())
    if (1 <= K <= 45):
        break
    else:
        print("Invalid input!")

a = 1
b = 0

for _ in range(K):
    new_a = b
    new_b = a + b
    a = new_a
    b = new_b

print(a, b)