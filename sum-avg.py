import sys
if len(sys.argv) > 1:
    scores = list(map(int, sys.argv[1:]))
    print("User provided scores:")
else:
    scores = [10, 20, 30, 40, 50]  
    print("No input given - using default scores:")
total = sum(scores)
average = total / len(scores)
maximum = max(scores)
minimum = min(scores)

print("Scores =", scores)
print("Sum =", total)
print("Average =", average)
print("Maximum =", maximum)
print("Minimum =", minimum)
