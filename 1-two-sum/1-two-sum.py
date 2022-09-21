class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumTarget = {c : i for i,c in enumerate(nums)}
        print(sumTarget)
        for n in range(len(nums)):
            diff = target - nums[n]
            print (diff)
            if diff in sumTarget and sumTarget[diff] != n:
                return [sumTarget[diff], n] 
            else:
                continue
        return
    
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        for i in range(len(nums)):
            diff = (target - nums[i])
            if diff in numMap:
                return(numMap[diff], i)
            numMap[nums[i]] = i 
        return
'''