# Input:  Strings Pattern and Text, and an integer d
# Output: The number of times Pattern appears in Text with at most d mismatches
def ApproximatePatternCount(Pattern, Text, d):
    count = 0 # initialize count variable
    # your code here
    positions = [] # initializing list of positions
    for i in range(len(Text)-len(Pattern)+1):
        if HammingDistance(Text[i:i+len(Pattern)], Pattern)<=d:
            positions.append(i)
            count=count+1
    return count


# Insert your HammingDistance function on the following line.
def HammingDistance(p, q):
    # your code here
    hamming=0
    for i in range(len(p)):
        if p[i]!=q[i]:
            hamming=hamming+1
    return hamming

### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys
lines = sys.stdin.read().splitlines()
print(ApproximatePatternCount(lines[0],lines[1],int(lines[2])))