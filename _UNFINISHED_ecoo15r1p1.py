# ecoo15r1p1

# Initialize box and n of lines
box = []
n = 0

# Initialize color count, handful count, non_red_count, red_count, and seconds
color_count = 0
handful_count = 0
non_red_count = 0
red_count = 0
seconds = 0

# Initialize smartie color count
colors = {
    'orange': 0,
    'blue': 0,
    'green': 0,
    'yellow': 0,
    'pink': 0,
    'violet': 0,
    'brown': 0,
    'red': 0
}

# Get input
while True:
    color = str(input())
    box.append(color)
    n += 1

    # Break out of loop once 'out of box' is detected
    if color == 'end of box':
        break

# Validate that box contains valid number of smarties
if not (50 <= n <= 200):
    quit()

# Sort smarties by color
while True:
    for color in colors:
        for smartie in box:
            if smartie == color:
                box.remove(smartie)
                color_count += 1
                colors[f"{color}"] = color_count
    if smartie == 'end of box':
        break

# Verify all colors have been sorted
print(colors)


# Separate red from the rest # This needs to be fixed we are eating each color at a time
for color in colors:
    if color != 'red':
        non_red_count += colors[f"{color}"]
    elif color == 'red':
        red_count += colors[f"{color}"]

while non_red_count != 0:
    for i in range(non_red_count):
        # Add smartie to hand and remove from non_red_count
        handful_count += 1
        non_red_count -= 1

        # Perform action once hand is full
        if handful_count == 7:
            seconds += 13
            handful_count = 0

# Add 16 seconds for each red smartie
seconds += (red_count * 16)

# Convert to minutes
mins = seconds / 60

# Print total time in seconds to eat all smarties
print(mins)