def roman_int(s,l={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}):
    if len(s)==1:
        return l[s[0]]
    if l[s[0]]<l[s[1]]:
        return roman_int(s[1:])-l[s[0]]
    return roman_int(s[1:])+l[s[0]]
    

print(roman_int("III"))