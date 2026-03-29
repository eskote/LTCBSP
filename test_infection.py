p = int(input())
n = int(input())
r = int(input())

total = n
new = n
day = 0

while total <= p:
    day += 1
    new *= r
    total += new

print(day)