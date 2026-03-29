# ccc07j1

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