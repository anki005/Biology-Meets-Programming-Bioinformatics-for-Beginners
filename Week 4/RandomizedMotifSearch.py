# import the random package here
import random

# Input:  Positive integers k and t, followed by a list of strings Dna
# Output: RandomizedMotifSearch(Dna, k, t)
def RandomizedMotifSearch(Dna, k, t):
    # insert your code here
    M = RandomMotifs(Dna, k, t)
    BestMotifs = M

    while True:
        Profile = ProfileWithPseudocounts(M)
        M = Motifs(Profile, k, Dna)
        if Score(M) < Score(BestMotifs):
            BestMotifs = M
        else:
            return BestMotifs 

# Insert necessary subroutines here, including RandomMotifs(), ProfileWithPseudocounts(), Motifs(), Score(),
# and any subroutines that these functions need.
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

def Score(Motifs):
    # Insert code here
    consensus=Consensus(Motifs)
    score=0
    for j in range(len(Motifs[0])):
        for i in range(len(Motifs)):
            if Motifs[i][j]!=consensus[j]:
                score+=1
    return score


def Consensus(Motifs):
    # insert your code here
    k = len(Motifs[0])
    count = CountWithPseudocounts(Motifs)
    consensus = ""
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus

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


def RandomMotifs(Dna, k, t):
    # place your code here.
    motifs=[]
    for i in range(t):
        n = random.randint(0, len(Dna[0])-k)
        motifs.append(Dna[i][n:n+k])
    return motifs

def Motifs(Profile, k, Dna):
    # insert your code here
    kmers = []
    for i in Dna:
        kmer = ProfileMostProbableKmer(i, k, Profile)
        kmers.append(kmer)
    return kmers

def ProfileMostProbableKmer(text, k, profile):
    max_pr=-1
    k_mer=""
    for i in range(len(text)-k+1):
        if Pr(text[i:i+k], profile) > max_pr:
            max_pr = Pr(text[i:i+k], profile)
            k_mer = text[i:i+k]
    return k_mer

def Pr(Text, Profile):
    p=1
    for i in range(len(Text)):
        p=p*Profile[Text[i]][i]
    return p


k = 8
t = 5
Dna = ["CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA", "GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG", "TAGTACCGAGACCGAAAGAAGTATACAGGCGT",
"TAGATCAAGTTTCAGGTGCACGTCGGTGAACC", "AATCCACCAGCTCCACGTGCAATGTTGGCCTA"]