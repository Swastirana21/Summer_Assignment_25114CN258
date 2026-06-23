# Check anagram strings 
def check_anagram(s1,s2):
    if len(s1)!=len(s2):
        return "Not anagrams"
    freq={}
    for char in s1:
        if char in freq:
            freq[char]+=1
        else:
            freq[char]=1
    for char in s2:
        if char in freq:
            freq[char]-=1
        else:
            return "Not anagrams"
        


    for val in freq.values():
        if val!=0:
            return "Not anagrams"
    return "Yes,they are anagrams"
s1="listen"
s2="silent"
print(check_anagram(s1,s2))
