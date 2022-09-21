class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        hashS , hashT = {}, {}
        
        if len(s) != len(t):
            return False
        
        
        for i in range(len(s)):
            hashS[s[i]] = 1 + hashS.get(s[i], 0)
            hashT[t[i]] = 1 + hashT.get(t[i], 0)
            
        for key in hashS:
            if hashS[key] != hashT.get(key, 0):
                return False
            
        return True
                