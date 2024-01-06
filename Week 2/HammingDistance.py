def HammingDistance(p, q):
    # your code here
    hamming=0
    for i in range(len(p)):
        if p[i]!=q[i]:
            hamming=hamming+1
    return hamming


p='CTTGAAGTGGACCTCTAGTTCCTCTACAAAGAACAGGTTGACCTGTCGCGAAG'
q='ATGCCTTACCTAGATGCAATGACGGACGTATTCCTTTTGCCTCAACGGCTCCT'
print(HammingDistance(p,q))
'''
a=list(range(5))
b=a
a[2]=12
print(b)'''