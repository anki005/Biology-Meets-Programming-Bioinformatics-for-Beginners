# Input:  A string Pattern
# Output: The reverse of Pattern
def Reverse(Pattern):
    # your code here
    str=""
    for char in Pattern:
        str=char+str
    return str