import itertools

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        val= []
        freq = []
        out = []
        
        for i in range(len(nums)):
            if i % 2 == 0 :
                val.append(nums[i])
            else:
                freq.append(nums[i])
                
        for j in range(len(val)):
            out.append(list(itertools.repeat(freq[j], val[j])))
            #print(out)
            
        return list(itertools.chain.from_iterable(out))