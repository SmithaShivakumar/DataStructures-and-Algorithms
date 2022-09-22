from collections import Counter 
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashA = Counter(ransomNote)
        hashB = Counter(magazine)

        
        return not hashA - hashB
            
        
        '''        flag = False
        
        for i in hashB:
            if hashB[i] == hashA.get(i,0):
                flag = True'''