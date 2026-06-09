class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        count1={}
        count2={}
        for char in range(len(s)):
            count1[s[char]]=count1.get(s[char],0)+1
            count2[t[char]]=count2.get(t[char],0)+1

        if count1==count2:
            return True
        else:
            return False