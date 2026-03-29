# ccc19j3

# Number of lines that will follow
n = int(input())

# Initialize runs
runs = 0

# Initialize result_set
result_set = []

# count consecutive chars function
def count_consecutive_chars(s: str):
    if not s:
        exit()
    result = []
    current_char = s[0]
    count = 1

    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            result.append((count, current_char))
            # Reset current char and count if char does not repeat
            current_char = char
            count = 1
    
    # Don't forget the last group
    result.append((count, current_char))
    result_set.append(result)

# Run function for n times based on input
for i in range(0, n):
    word = str(input())
    count_consecutive_chars(word)
    
for set in result_set:
    temp_string = ''
    for key, value in set:
        temp_string += f"{key} {value} "
    print(temp_string)