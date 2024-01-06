# first, import the random package
import random
# then, copy Pr, Normalize, and WeightedDie below this line
def WeightedDie(Probabilities):
    kmer = '' # output variable
    # your code here
    p = random.uniform(0, 1)
    sum=0.0
    for kmer, prob in Probabilities.items():
        sum+=prob
        if p<=sum:
           return kmer
    
def Normalize(Probabilities):
    # your code here
    sum=0.0
    for i in Probabilities.values():
        sum+=i
    for i in Probabilities.keys():
        Probabilities[i]/=sum
    return Probabilities

def Pr(Text, Profile):
    p=1
    for i in range(len(Text)):
        p=p*Profile[Text[i]][i]
    return p
# Input:  A string Text, a profile matrix Profile, and an integer k
# Output: ProfileGeneratedString(Text, profile, k)
def ProfileGeneratedString(Text, profile, k):
    # your code here
    n = len(Text)
    probabilities = {}
    for i in range(0,n-k+1):
        probabilities[Text[i:i+k]] = Pr(Text[i:i+k], profile)
    probabilities = Normalize(probabilities)
    return WeightedDie(probabilities)