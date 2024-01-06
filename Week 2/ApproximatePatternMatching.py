# Input:  Strings Pattern and Text along with an integer d
# Output: A list containing all starting positions where Pattern appears
# as a substring of Text with at most d mismatches
def ApproximatePatternMatching(Text, Pattern, d):
    positions = [] # initializing list of positions
    # your code here
    for i in range(len(Text)-len(Pattern)+1):
        if HammingDistance(Text[i:i+len(Pattern)], Pattern)<=d:
            positions.append(i)
    return positions


# Insert your Hamming distance function on the following line.
def HammingDistance(p, q):
    # your code here
    hamming=0
    for i in range(len(p)):
        if p[i]!=q[i]:
            hamming=hamming+1
    return hamming

Pattern='AAAAA'
Text='AACAAGCATAAACATTAAAGAG'
d=1
print(ApproximatePatternMatching(Text, Pattern, d))