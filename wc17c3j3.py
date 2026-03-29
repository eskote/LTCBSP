# wc17c3j3

password = str(input())
if len(password) > 7 and len(password) < 13 and password.isalnum():
    count_upper = 0
    count_lower = 0
    count_digit = 0
    for char in password:
        if char.islower():
            count_lower += 1
        elif char.isupper():
            count_upper += 1
        elif char.isdigit():
            count_digit += 1
    if count_lower >= 3 and count_upper >= 2 and count_digit >= 1:
        print("Valid")
    else:
        print("Invalid")
else:
    print("Invalid")

