class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        suml,  sumr = 0, sum(nums) 
        for index in range(len(nums)):
            sumr -= nums[index]
            if suml == sumr:
                return index
            suml += nums[index]            
        return -1