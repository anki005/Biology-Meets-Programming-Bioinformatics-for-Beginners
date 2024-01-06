# Input:  A profile matrix Profile and a list of strings Dna
# Output: Motifs(Profile, Dna)
def Motifs(Profile, Dna):
    # insert your code here
    kmers = []
    for i in Dna:
        kmer = ProfileMostProbableKmer(i, 4, Profile)
        kmers.append(kmer)
    return kmers

# Insert your ProfileMostProbablePattern(Text, k, Profile) and Pr(Pattern, Profile) functions here.
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