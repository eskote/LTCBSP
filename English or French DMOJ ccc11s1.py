# English or French DMOJ ccc11s1

# Canadian Computing Competition: 2011 Stage 1, Senior #1

# You would like to do some experiments in natural language processing. 
# Natural language processing (NLP) involves using machines to recognize human languages.

# Your first idea is to write a program that can distinguish English text from French text.

# After some analysis, you have concluded that a very reasonable way of distinguishing these two languages is to compare the occurrences of the 
# letters t and T to the occurrences of the letters s and S. Specifically:

#     if the given text has more t and T characters than s and S characters, we will say that it is (probably) English text;
#     if the given text has more s and S characters than t and T characters, we will say that it is (probably) French text;
#     if the number of t and T characters is the same as the number of s and S characters, we will say that it is (probably) French text.

# Input Specification

# The input will contain the number N ( 0 < N < 10 000 ) followed by N lines of text, 
# where each line has at least one character and no more than 100 characters.
# Output Specification

# Your output will be one line. This line will either consist of the word English 
# (indicating the text is probably English) or French (indicating the text is probably French).

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