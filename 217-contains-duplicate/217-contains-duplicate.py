from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:   
        numCount = Counter(nums)
        for i in range(len(nums)):
            if numCount[nums[i]] > 1:
                return True
        return False