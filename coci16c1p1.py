# coci16c1p1

while True:
    monthly_mb = int(input())
    if (1 <= monthly_mb <= 100):
        break
    else:
        print("Please enter a number between 1-100")

while True:
    N = int(input())
    if (1 <= N <= 100):
        break
    else:
        print("Please enter a number between 1-100")

excess = 0
for i in range(N):
    used = int(input())
    excess = excess + monthly_mb - used

print(excess + monthly_mb)

