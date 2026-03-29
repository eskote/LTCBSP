#  wc15c2j1

N = int(input())

if N <= 1:
    N = "far"
elif N <= 5:
    N = ("far" + ((N - 1) * ", far"))
print("A long time ago in a galaxy " + N + " away...")