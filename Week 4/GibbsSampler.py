####  Psseudocode ####
'''
  GibbsSampler(Dna, k, t, N)
        randomly select k-mers Motifs = (Motif1, …, Motift) in each string from Dna
        BestMotifs ← Motifs
        for j ← 1 to N
            i ← randomly generated integer between 1 and t
            Profile ← profile matrix formed from all strings in Motifs except for Motifi
            Motifi ← Profile-randomly generated k-mer in the i-th string
            if Score(Motifs) < Score(BestMotifs)
                BestMotifs ← Motifs
        return BestMotifs
'''


# first, import the random package
import random

# Input:  Integers k, t, and N, followed by a collection of strings Dna
# Output: GibbsSampler(Dna, k, t, N)
def GibbsSampler(Dna, k, t, N):
    BestMotifs = [] # output variable
    # your code here
    Motifs = RandomMotifs(Dna, k, t)
    BestMotifs = Motifs
    for j in range(1,N+1):
        i = random.randint(1, t-1)
        Motifs.pop(i)
        Profile = ProfileWithPseudocounts(Motifs)
        motifi = ProfileRandomKmer(Dna, k, Profile, i)
        Motifs.insert(i, motifi)
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs

# place all subroutines needed for GibbsSampler below this line
def RandomMotifs(Dna, k, t):
    # place your code here.
    motifs=[]
    for i in range(t):
        n = random.randint(0, len(Dna[0])-k)
        motifs.append(Dna[i][n:n+k])
    return motifs

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

def ProfileRandomKmer(text, k, profile, x):
    score = []
    kmer = ""
    prob=1
    for i in range(len(text)-k+1):
        kmer = text[x][i:i+k]
    for i in range(len(kmer)):
        prob=prob*profile[kmer[i]][i]
    score.append(prob)
    random_pr = random.uniform(0, sum(score))
    recent=0
    for index, value in enumerate(score):
        recent+=value
        if random_pr <= recent:
            return text[x][index:index+k]


#Test case 
Dna = ["CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA","GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG","TAGTACCGAGACCGAAAGAAGTATACAGGCGT",
       "TAGATCAAGTTTCAGGTGCACGTCGGTGAACC","AATCCACCAGCTCCACGTGCAATGTTGGCCTA"]
k = 8
t = 5
N = 100
print(GibbsSampler(Dna, k, t, N))