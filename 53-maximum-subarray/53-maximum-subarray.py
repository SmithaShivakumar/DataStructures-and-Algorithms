class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        out = 0
        maxSub = nums[0]
        for n in range(len(nums)):
            if out < 0 :
                out = 0         
            out += nums[n]
            maxSub = max(maxSub, out)
        return maxSub