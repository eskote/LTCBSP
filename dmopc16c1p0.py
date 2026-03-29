# dmopc16c1p0

while True:
    W = int(input())
    if (1 <= W <= 3):
        break
    else:
        print("please enter the width of the pizza 1-3")

while True:
    C = int(input())
    if (0 <= C <= 100):
        break
    else:
        print("Please enter the extra-cheesiness between 1-100")

if W == 3 and C >= 95:
    S = "absolutely"
elif W ==1 and C <= 50:
    S = "fairly"
else:
    S = "very"

print(f"C.C. is {S} satisfied with her pizza.")