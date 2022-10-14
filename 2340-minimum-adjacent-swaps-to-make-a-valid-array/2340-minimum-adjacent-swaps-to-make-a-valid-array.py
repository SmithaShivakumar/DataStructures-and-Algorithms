class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        res = 0
        max_val = max(nums)
        min_val = min(nums)
        
        max_index = 0
		# find first occurence of the min
        min_index = nums.index(min_val)
        # find last occurence of the max
        for i, val in enumerate(nums):
            if val == max_val:
                max_index = i
        
        if max_index == min_index:
            return 0
        
		# if the min index is greater than max_index, swap the 2
        if min_index > max_index:
            res += abs(max_index - min_index) * 2 - 1
            max_index, min_index = min_index, max_index
         
        res += len(nums) - max_index - 1
        res += min_index
        
        return res