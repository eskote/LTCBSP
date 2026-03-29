# Canadian Calorie Counting DMOJ ccc06j1

# Canadian Computing Competition: 2006 Stage 1, Junior #1

# At Chip's Fast Food emporium there is a very simple menu. Each food item is selected by entering a digit choice.
# Here are the three burger choices:
# 1 – Cheeseburger (461 Calories)
# 2 – Fish Burger (431 Calories)
# 3 – Veggie Burger (420 Calories)
# 4 – no burger 	Here are the three drink choices:
# 1 – Soft Drink (130 Calories)
# 2 – Orange Juice (160 Calories)
# 3 – Milk (118 Calories)
# 4 – no drink
# Here are the three side order choices:
# 1 – Fries (100 Calories)
# 2 – Baked Potato (57 Calories)
# 3 – Chef Salad (70 Calories)
# 4 – no side order 	Here are the three dessert choices:
# 1 – Apple Pie (167 Calories)
# 2 – Sundae (266 Calories)
# 3 – Fruit Cup (75 Calories)
# 4 – no dessert

# Write a program that will compute the total Calories of a meal.
# Input Specification

# The program should input a number for each type of item then calculate and display the Calorie total. 
# The first line will be the customer's choice of burger, the second will be the choice of side, then drink, then dessert. 
# You may assume that each input will be a number from 1 to 4. 
# That is, each customer has to pick exactly one number from each of the four options out of each of the four categories.
# Output Specification

# The program prints out the total Calories of the selected meal, and stops executing after this output.


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