# Input:  A DNA string Pattern
# Output: The complementary string of Pattern (with every nucleotide replaced by its complement).
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
