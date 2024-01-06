# Input:  A DNA string Pattern
# Output: The reverse complement of Pattern
def ReverseComplement(Pattern):   
    # your code here
    Pattern = Reverse(Pattern)
    Pattern = Complement(Pattern)
    return Pattern

# Copy your Reverse() function here.
def Reverse(Pattern):
    # your code here
    str=""
    for char in Pattern:
        str=char+str
    return str

# Copy your Complement() function here.
def Complement(Pattern):
    # your code here
    str=""
    for char in Pattern:
        if char=="A":
            str=str+"T"
        elif char=="C":
            str=str+"G"
        elif char=="T":
            str=str+"A"
        elif char=="G":
            str=str+"C"
    return str