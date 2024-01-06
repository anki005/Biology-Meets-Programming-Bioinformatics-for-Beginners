# Insert your Pr(text, profile) function here from Motifs.py.
def Pr(Text, Profile):
    # insert your code here
    p=1
    for i in range(len(Text)):
        p=p*Profile[Text[i]][i]
    return p
# Write your ProfileMostProbableKmer() function here.
# The profile matrix assumes that the first row corresponds to A, the second corresponds to C,
# the third corresponds to G, and the fourth corresponds to T.
# You should represent the profile matrix as a dictionary whose keys are 'A', 'C', 'G', and 'T' and whose values are lists of floats
def ProfileMostProbableKmer(text, k, profile):
    max_pr=-1
    k_mer=""
    for i in range(len(text)-k+1):
        if Pr(text[i:i+k], profile) > max_pr:
            max_pr = Pr(text[i:i+k], profile)
            k_mer = text[i:i+k]
    return k_mer