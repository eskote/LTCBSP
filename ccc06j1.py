# Canadian Calorie Counting DMOJ ccc06j1

# Input Burger Item
while True:
    B = int(input())
    if (0 < B < 5):
        break
    print("Please input a burger item 1-4.")

# Input Side Item
while True:
    S = int(input())
    if (0 < S < 5):
        break
    print("Please enter a side item 1-4.")

# Input Drink Item
while True:
    D = int(input())
    if (0 < D < 5):
        break
    print("Please enter a drink item 1-4.")

# Input Dessert Item
while True:
    DS = int(input())
    if (0 < DS < 5):
        break
    print("Please enter a dessert item 1-4.")

# Calculate Calories for Burger Item
if B == 1:
    B = 461
elif B == 2:
    B = 431
elif B == 3:
    B = 420
elif B == 4:
    B = 0

# Calculate Side Item Calories
if S == 1:
    S = 100
elif S ==2:
    S = 57
elif S ==3:
    S = 70
elif S == 4:
    S = 0

#Calculate Drink Item Calories
if D == 1:
    D = 130
elif D == 2:
    D = 160
elif D == 3:
    D = 118
elif D == 4:
    D = 0

# Calculate Dessert Item Calories
if DS == 1:
    DS = 167
elif DS == 2:
    DS = 266
elif DS == 3:
    DS = 75
elif DS == 4:
    DS = 0

CC = B + S + D + DS
print(f"Your total Calorie count is {CC}.")