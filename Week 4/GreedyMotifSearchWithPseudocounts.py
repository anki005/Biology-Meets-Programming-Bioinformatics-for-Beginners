# Input:  A list of kmers Dna, and integers k and t (where t is the number of kmers in Dna)
# Output: GreedyMotifSearch(Dna, k, t)
def GreedyMotifSearchWithPseudocounts(Dna, k, t):
    BestMotifs = [] # output variable
    # your code here
    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])
    
    n = len(Dna[0])
    for i in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][i:i+k])
        for j in range(1, t):
            P = ProfileWithPseudocounts(Motifs[0:j])
            Motifs.append(ProfileMostProbableKmer(Dna[j], k, P))
        if Score(Motifs) < Score(BestMotifs):
                    BestMotifs = Motifs
    return BestMotifs

# Copy all needed subroutines here.  These subroutines are the same used by GreedyMotifSearch(),
# except that you should replace Count(Motifs) and Profile(Motifs) with the new functions
# CountWithPseudocounts(Motifs) and ProfileWithPseudocounts(Motifs).
def Score(Motifs):
    # Insert code here
    consensus=Consensus(Motifs)
    score=0
    for j in range(len(Motifs[0])):
        for i in range(len(Motifs)):
            if Motifs[i][j]!=consensus[j]:
                score+=1
    return score

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
# Then copy your ProfileMostProbableKmer(Text, k, Profile) and Pr(Text, Profile) functions here.
def Pr(Text, Profile):
    # insert your code here
    p=1
    for i in range(len(Text)):
        p=p*Profile[Text[i]][i]
    return p

def ProfileMostProbableKmer(text, k, profile):
    max_pr=-1
    k_mer=""
    for i in range(len(text)-k+1):
        if Pr(text[i:i+k], profile) > max_pr:
            max_pr = Pr(text[i:i+k], profile)
            k_mer = text[i:i+k]
    return k_mer