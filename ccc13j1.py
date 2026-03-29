# ccc13j1

while True:
    Y = int(input())
    if (0 <= Y <= 50):
        break
    else:
        print("Enter a valid age inside the range (0-50)")

while True:
    M = int(input())
    if (Y <= M <= 50):
        break
    else:
        print("Enter a valid age inside the range (0-50)")

O = M + (M - Y)
print(O)
