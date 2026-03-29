num_q = int(input())
answ = str(input())

# Take only the first 'num_q' chars
answers = answ[:num_q]

# The three repeating patterns
adrian = 'ABC'
bruno = "BABC"
goran = "CCAABB"

aa = 0
bb = 0
gg = 0

for i in range(num_q):

    ans = answers[i]

    if ans == adrian[i % 3]:
        aa += 1
    
    if ans == bruno[i % 3]:
        bb += 1
    
    if ans == goran[i % 3]:
        gg += 1

# Find the max score
max_score = max(aa, bb, gg)

print(max_score)

if aa == max_score:
    print("Adrian")

if bb == max_score:
    print("Bruno")

if gg == max_score:
    print("Goran")