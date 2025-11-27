import sys
if len(sys.argv) > 1:
    scores = list(map(int, sys.argv[1:]))
    print("User provided scores:")
else:
    scores = [10, 20, 30, 40, 50]  
    print("No input given - using default scores:")
total = sum(scores)
average = total / len(scores)

print("Scores =", scores)
print("Sum =", total)
print("Average =", average)
