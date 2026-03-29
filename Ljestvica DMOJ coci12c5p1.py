# Ljestvica DMOJ coci12c5p1

# Veronica attends a music academy. She was given a music sheet of a composition with only notes (without annotations), 
# and needs to recognise the scale used. In this problem, we will limit ourselves to only the two most frequently used 
# (and usually taught in schools first) scales: A -minor and C -major. This doesn't make them simpler or more basic than other minor and major scales – 
# all minor scales are mutually equivalent save for translation, and so are major scales.

# Still, out of the 12 tones of an octave { A , A # , B , C , C # , D , D # , E , F , F # , G , G # } used in modern music, 
# A -minor and C -major scales do use the tones with shortest names: A -minor is defined as an ordered septuple ( A , B , C , D , E , F , G ) , 
# and C -major as ( C , D , E , F , G , A , B ) .

# Notice that the sets of tones of these two scales are equal. What's the difference? 
# The catch is that not only the set of tones, but also their usage, determines a scale. 
# Specifically, the tonic (the first tone of a scale), 
# subdominant (the fourth tone) and dominant (the fifth tone) are the primary candidates for accented tones in a composition. 
# In A -minor, these are A , D , and E , and in C -major, they are C , F , and G . We will name these tones main tones.

# Aren't the scales still equivalent save for translation? 
# They are not: for example, the third tone of A -minor ( C ) is three half-tones higher than the tonic ( A ) , 
# while the third tone of C -major ( E ) is four halftones higher than the tonic ( C ) . The difference, therefore, lies in the intervals. 
# This makes minor scales "sad" and major scales "happy".

# Write a program to decide if a composition is more likely written in A -minor or C -major 
# by counting whether there are more main tones of A -minor or of C -major among the accented tones (the first tones in each measure). 
# If there is an equal number of main tones, 
# determine the scale based on the last tone (which is guaranteed to be either A for A -minor or C for C -major in any such test case).

# For example, examine the well-known melody "Frère Jacques":

# C D | E C | C D | E C | E F | G | E F | G | G A G F | E C | G A G F | E C | C G | C | C G | C

# The character | separates measures, so the accented tones are, in order: C , E , C , E , E , G , E , G , G , E , G , E , C , C , C , C . 
# Ten of them ( C , C , G , G , G , G , C , C , C , C ) are main tones of C -major, 
# while six ( E , E , E , E , E , E ) are main tones of A -minor. Therefore, our best estimate is that the song was written in C -major.
# Input Specification

# The first and only line of input contains a sequence of at least 2 , 
# and at most 100 , characters from the set { A, B, C, D, E, F, G, | } . 
# This is a simplified notation for a composition, where the character | separates measures. 
# The characters | will never appear adjacent to one another, at the beginning, or at the end of the sequence.
# Output Specification

# The first and only line of output must contain the text C-dur (for C -major) or A-mol (for A -minor).

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

# print(f"Total C notes: {c_major}")
# print(f"Total A notes: {a_minor}")
# if last_note is None:
#      print("Last note is null")
# else:
#     print(f"Last tone is: {last_note}")

if c_major > a_minor:
    print("C-dur")
elif c_major < a_minor:
    print("A-mol")
elif c_major == a_minor:
    if last_note in c_major_notes:
        print("C-dur")
    elif last_note in a_minor_notes:
        print("A-mol")
