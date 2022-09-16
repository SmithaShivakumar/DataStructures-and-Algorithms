class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = []
        temp = 0
        for i in range(len(nums)):
            temp += nums[i]
            running_sum.append(temp)
        return running_sum