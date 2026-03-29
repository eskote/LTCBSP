# wc17c1j2

while True:
    C = int(input())
    if (-40 <= C <= 40):
        break
    else: print("Enter a valid temp between (-40 and 40)")

# Convert between Farenheit and Celcius
F = ((9 / 5) * C) + 32
print(F)