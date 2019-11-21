def firstNotRepeatingCharacter(s):
    
    for val in s:
        print val
        print s.index(val)
        print s.rindex(val)
        if s.index(val) == s.rindex(val):
            return val
    return ("_")


s="abacaa"
print firstNotRepeatingCharacter(s)
