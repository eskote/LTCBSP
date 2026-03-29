# ecoo13r1p1

# Initialize activity, and get first number
activity = ''
late_students = 0
checked_out = 0
in_line = 0
allowed = {'TAKE', 'SERVE', 'CLOSE', 'EOF'}

next_number = int(input())
if not (0 < next_number < 999):
    quit()

while activity != 'EOF':
    # Input activity types
    # There can be up to 1 million lines of input 
    activity = input().strip()
    if activity not in allowed:
        quit()
    next_number += 1
    # Track activity
    if activity == 'TAKE':
        late_students += 1
    elif activity == 'SERVE':
        checked_out += 1
    elif activity == 'CLOSE':
        in_line = late_students - checked_out
        print(
            f"{late_students} {in_line} {next_number}"
        )
        # Reset values
        late_students = 0
        in_line = 0
        checked_out = 0

    # Reset next number if 999
    if next_number == 999:
        next_number = 1
    
    if activity == 'EOF':
        break