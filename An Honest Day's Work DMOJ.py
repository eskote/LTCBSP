# An Honest Day's Work DMOJ wc18c3j1

# Jessie, James, and Meowth, members of the honourable Team Rocket, have unfortunately fallen on hard times.
# With their funds necessarily allocated to constructing all manner of giant robots and other devices, they've been having difficulty affording any food lately.
# But that's nothing that an honest day's work can't fix!

# James has a can of leftover paint, containing P ( 1 ≤ P ≤ 100 ) litres of the stuff. When combined with his boundless collection of bottlecaps,
# this can result in some high-quality wares. When a bottlecap is artfully covered with B ( 1 ≤ B ≤ 100 ) litres of paint, it turns into a completely legitimate,
# Pokémon league-certified gym badge!

# James will produce as many badges as he can using the paint, using exactly B litres each. Pokémon trainers love their gym badges,
# so each such badge is sure to sell for D ( 1 ≤ D ≤ 100 ) Pokédollars.

# There might still be some extra paint left over, once there's not enough for another complete badge. However, there's no need for it to go to waste -
# James will sell any remaining paint at a rate of 1 Pokédollar per litre.

# How much money will James make for Team Rocket in total, from his sales of badges and leftover paint? Hopefully it'll be enough for at least a loaf of bread!
# Input Specification

# The first line of input consists of a single integer, P .
# The second line consists of a single integer, B .
# The third line consists of a single integer, D .
# Output Specification

# Output a single integer, the amount of money which James will make (in Pokédollars).

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