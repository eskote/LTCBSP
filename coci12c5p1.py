# coci12c5p1

# Input string
while True:
    song = str(input())
    # Strip whitespace
    song = song.replace(" ","")
    song_length = len(song)
    #print(f"Song length: {song_length}")
    if (1 < song_length < 101) and set(song).issubset("ABCDEFG| "):
        break
    else:
        print("Please enter between 1 and 100 notes and notes ABCDEFG|")

# Count 
c_major = 0
a_minor = 0

# Notes in each scale
a_minor_notes = {"A", "D", "E"}
c_major_notes = {"C", "F", "G"}

# Determines if current note is at the start of the measure
start_of_measure = True

# Stores the last note of the song in the event there is a tie between c_major and a_minor
last_note = song[-1]

# Start the loop
for note in song:
    if start_of_measure == True and note in c_major_notes:
        c_major += 1
        start_of_measure = False
    elif start_of_measure == True and note in a_minor_notes:
        a_minor += 1
        start_of_measure = False
    elif note == "|":
        start_of_measure = True
    else:
        start_of_measure = False

# Evaluate Results
if c_major > a_minor:
    print("C-dur")
elif c_major < a_minor:
    print("A-mol")
elif c_major == a_minor:
    if last_note in c_major_notes:
        print("C-dur")
    elif last_note in a_minor_notes:
        print("A-mol")
