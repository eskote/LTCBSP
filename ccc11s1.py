# English or French DMOJ ccc11s1

# Number of lines of text input
while True:
    number_of_lines = int(input())
    if (0 <= number_of_lines <= 10000):
        break
    else:
        print("Please input between 1 and 10000 lines.")

# Count of Ts and Ss
t_count = 0
s_count = 0
counted_lines = 0
while True:
    if counted_lines < number_of_lines:
        # Input lines of text
        line = str(input())
        for char in line:
            if char == "T":
                t_count += 1
            elif char == "t":
                t_count += 1
            elif char == "S":
                s_count += 1
            elif char == "s":
                s_count += 1
        counted_lines += 1
    else:
        break

# Print Results
if t_count < s_count:
    print("French")
elif t_count > s_count:
    print("English")
elif t_count == s_count:
    print("French")