# Input:  A set of kmers Motifs
# Output: ProfileWithPseudocounts(Motifs)
def ProfileWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {} # output variable
    # your code here
    profile = CountWithPseudocounts(Motifs)    
    for symbols in profile.keys():
        for values in range(len(profile[symbols])):
            profile[symbols][values]=profile[symbols][values]/float(t+4)
    return profile

# Input:  A set of kmers Motifs
# Output: CountWithPseudocounts(Motifs)
# HINT:   You need to use CountWithPseudocounts as a subroutine of ProfileWithPseudocounts
def CountWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    count = {} # output variable
    # your code here
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
             count[symbol].append(1)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count