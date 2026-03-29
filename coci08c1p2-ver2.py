num_ans = int(input())
answers = input().strip()[:num_ans]   # safe read + trim

adrian = "ABC"
bruno = "BABC"
goran = "CCAABB"

aa = bb = gg = 0

for i in range(num_ans):
    ans = answers[i]
    
    if ans == adrian[i % 3]:
        aa += 1
    if ans == bruno[i % 4]:
        bb += 1
    if ans == goran[i % 6]:
        gg += 1

top = max(aa, bb, gg)
print(top)

if aa == top:
    print("Adrian")
if bb == top:
    print("Bruno")
if gg == top:
    print("Goran")