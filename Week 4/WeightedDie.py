# first, import the random package
import random
# Input:  A dictionary Probabilities whose keys are k-mers and whose values are the probabilities of these kmers
# Output: A randomly chosen k-mer with respect to the values in Probabilities
def WeightedDie(Probabilities):
    kmer = '' # output variable
    # your code here
    p = random.uniform(0, 1)
    sum=0.0
    for kmer, prob in Probabilities.items():
        sum+=prob
        if p<=sum:
           return kmer