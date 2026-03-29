p = int(input())
n = int(input())
r = int(input())

total_infected = n
new_infected = n
day = 0

while total_infected <= p:
    day += 1
    new_infected *= r
    total_infected += new_infected

print(day)