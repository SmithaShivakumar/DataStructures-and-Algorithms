class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        def helperSum(arr):
            N = len(arr)
            row = [0]*(N-1)
            for i in range(N-1):
                row[i] = (arr[i] + arr[i+1]) % 10
            return row
            
        while len(nums) > 1:
            nums = helperSum(nums)
        return nums[0]