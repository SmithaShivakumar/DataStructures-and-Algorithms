from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:   
        numCount = Counter(nums)
        for i in range(len(nums)):
            if numCount[nums[i]] > 1:
                return True
        return False
    
'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        countNums = {}
        for i in range(len(nums)):
            if nums[i] in countNums:
                return True
            else:
                countNums[nums[i]] = 1
        return False        
'''