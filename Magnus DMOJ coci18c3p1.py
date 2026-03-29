# Magnus DMOJ coci18c3p1

# Problem type

# Magnus lost a game of chess to Kile so he found comfort in competitive programming. 
# Very soon, he heard of the iconic COCI competition and decided to try his luck there.

# He wrote a mail to Kile: "Dear Kile, please, prepare me for COCI. Magnus".

# Kile replied: "You want to participate in COCI? All right, here's your warm-up task. 
# A series of four consecutive letters of some word that make up the subword HONI (Croatian acronym for COCI) is called the HONI-block. 
# I will send you the word of length N and you will throw out as many letters as you want (it might be none as well) 
# so that in the end there are as many HONI-blocks as possible in the word. Kile".

# Magnus was very worried and asked you, COCI competitive scene, for help. Help him determine the maximum number of HONI-blocks he can get in the final word.
# Input

# The first line contains a word of length N ( 1 ≤ N ≤ 100 000 ) , consisting of uppercase letters of the English alphabet.
# Output

# In the first and only line, print out the required number of HONI-blocks.

honi_block = str(input())[:100001]

honi_count = 0
stage = 0
for char in honi_block:
    if stage == 0 and char == 'H':
        stage = 1
    elif stage == 1 and char == 'O':
        stage = 2
    elif stage == 2 and char == 'N':
        stage = 3
    elif stage == 3 and char == 'I':
        honi_count += 1
        stage = 0

print(honi_count)
    
