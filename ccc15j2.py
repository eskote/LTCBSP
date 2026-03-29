# ccc15j2

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
