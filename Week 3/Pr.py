# Input:  String Text and profile matrix Profile
# Output: Pr(Text, Profile)
def Pr(Text, Profile):
    # insert your code here
    p=1
    for i in range(len(Text)):
        p=p*Profile[Text[i]][i]
    return p

