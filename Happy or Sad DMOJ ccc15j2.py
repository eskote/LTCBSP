# Happy or Sad DMOJ ccc15j2

# CCC '15 J2 - Happy or Sad

# We often include emoticons in our text messages to indicate how we are feeling. 
# The three consecutive characters :-) indicate a happy face and the three consecutive characters :-( indicate a sad face. 
# Write a program to determine the overall mood of a message.
# Input Specification

# There will be one line of input that contains between 1 and 255 characters.
# Output Specification

# The output is determined by the following rules:

#     If the input line does not contain any happy or sad emoticons, output none.
#     Otherwise, if the input line contains an equal number of happy and sad emoticons, output unsure.
#     Otherwise, if the input line contains more happy than sad emoticons, output happy.
#     Otherwise, if the input line contains more sad than happy emoticons, output sad.

message = input()[:256]

happy = ":-)"
sad = ":-("

count_happy = message.count(happy)
count_sad = message.count(sad)

if count_happy == 0 and count_sad == 0:
    print("none")
elif count_happy == count_sad:
    print("unsure")
elif count_happy < count_sad:
    print("sad")
elif count_happy > count_sad:
    print("happy")
