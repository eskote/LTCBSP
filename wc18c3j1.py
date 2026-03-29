# wc18c3j1

while True:
    P = int(input())
    if (1 <= P <= 100):
        break
    else: ("Please input a number that represents liters of paint (1-100)")
    
while True:
    B = int(input()) 
    if (1 <= B <= 100):
        break
    else: ("Please input the number of liters of paint for the bottlecap. (1-100)")

while True:
    D = int(input())
    if (1 <= D <= 100):
        break
    else: ("Please input the number of pokedollars. (1-100)")

# Calculate Profit

C = ( (P // B) * D ) # Calculate Number of badges he can paint
B = ( (P % B) * 1 ) # Calculate the leftover paint

print (C + B) # Total Profit