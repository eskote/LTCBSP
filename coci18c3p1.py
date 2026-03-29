# coci18c3p1

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
    
