# Input: A dictionary Probabilities, where keys are k-mers and values are the probabilities of these k-mers (which do not necessarily sum up to 1)
# Output: A normalized dictionary where the probability of each k-mer was divided by the sum of all k-mers' probabilities
def Normalize(Probabilities):
    # your code here
    sum=0.0
    for i in Probabilities.values():
        sum+=i
    for i in Probabilities.keys():
        Probabilities[i]/=sum
    return Probabilities
        