# coci13c3p1

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