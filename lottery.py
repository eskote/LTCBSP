# lottery
import random

winning_choices = {
    16,
    49,
    60,
    69,
    98,
    45,
    94,
    31,
    59,
    39,
    'b',
    'g',
    'm',
    'j',
    'a'
}

choices = {
    chr(random.randint(ord('a'), ord('z'))),
    chr(random.randint(ord('a'), ord('z'))),
    chr(random.randint(ord('a'), ord('z'))),
    chr(random.randint(ord('a'), ord('z'))),
    chr(random.randint(ord('a'), ord('z'))),
    int(random.randint(1, 100)),
    int(random.randint(1, 100)),
    int(random.randint(1, 100)),
    int(random.randint(1, 100)),
    int(random.randint(1, 100)),
    int(random.randint(1, 100)),
    int(random.randint(1, 100)),
    int(random.randint(1, 100)),
    int(random.randint(1, 100)),
    int(random.randint(1, 100))
}

my_win = 0
for choice in winning_choices:
    if choice in choices:
        print(
            f"Congratulations! Your chioce {choice} is a winner!"
        )
        print(
            f"It took {my_win} times to win!"
        )
        my_win = 0
    else:
        print(
            "Unfortunately your ticket did not win."
        )
        my_win += 1
