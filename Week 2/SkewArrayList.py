def SkewArray(Genome):
    # your code here
    skew=[]
    skew.append(0)
    count=0
    for i in Genome:
        if i=='C':
            count=count+1
            skew.append(skew[count-1]-1)
        elif i=='G':
            count=count+1
            skew.append(skew[count-1]+1)
        elif i=='A'or i=='T':
            count=count+1
            skew.append(skew[count-1])
    return skew
3
Genome = "TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT"
print(SkewArray(Genome))