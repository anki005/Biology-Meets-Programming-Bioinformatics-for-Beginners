def MinimumSkew(Genome):
    positions = [] # output variable
    # your code here
    skewed=SkewArray(Genome)
    sortskewed=dict(sorted(skewed.items(), key=lambda item:item[1]))
    low_value=list(sortskewed.values())[0]
    for i in sortskewed.keys():
        if sortskewed[i] == low_value:
            positions.append(i)
    return positions

# Input:  A String Genome
# Output: SkewArray(Genome)
# HINT:   This code should be taken from the last Code Challenge.
def SkewArray(Genome):
    skew = {} # output variable
    # your code here
    skew[0]=0
    count=0
    for i in Genome:
        if i=='C':
            count=count+1
            skew[count]=skew[count-1]-1
        elif i=='G':
            count=count+1
            skew[count]=skew[count-1]+1
        elif i=='A'or i=='T':
            count=count+1
            skew[count]=skew[count-1]
    return skew

Genome = "TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT"
print(MinimumSkew(Genome))