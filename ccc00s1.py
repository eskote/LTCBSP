# ccc00s1

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
    m2 += 1
    quarters -= 1
    plays += 1
    if quarters == 0:
        break
    if m2 == 100:
        quarters += 60
        m2 = 0
    m3 += 1
    quarters -= 1
    plays += 1
    if quarters == 0:
        break
    if m3 == 10:
        quarters += 9
        m3 = 0

print(f"Martha plays {plays} times before going broke.")