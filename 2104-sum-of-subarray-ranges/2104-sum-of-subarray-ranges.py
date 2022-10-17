class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        def sm(op): 
            final_sum = 0 
            stack = []
            for i in range(len(nums) + 1):
                # we're utilizing the stack to maintain ranges in which some
                # nums[x] is the largest or smallest element in the range, here's how:
                # if we're looking for max_sum, we pass in greater than so that
                # we pop off the stack until the current element nums[i] is not
                # greater than what's at the end of the stack currently
                # let's follow what happens to this i and denote it as x
                # the element to the left of x in the stack represents the left
                # boundary since we didn't pop it off, in other words it's larger than nums[x]
                # then when it is x's turn to get popped off we know that
                # nums[i] is larger than nums[x] therefore we can use i as
                # the right boundary
                # between the left boundary and the right boundary, nums[x]
                # is the largest element
                while stack and (i == len(nums) or op(nums[i], nums[stack[-1]])): 
                    mid = stack.pop()
                    right_boundary = i
                    left_boundary = stack[-1] if stack else -1
                    # there are (right_boundary - mid) * (mid - left_boundary)
                    # subarrays in which nums[mid] is the largest or smallest element
                    # depending on the operator passed in
                    final_sum += nums[mid] * (right_boundary - mid) * (mid - left_boundary)
                stack.append(i)
            return final_sum
        # the sum of all subarray ranges is (max_sum - min_sum) where:
        # max_sum is the sum of the max element of all possible subarrays
        # min_sum is the sum of the min element of all possible subarrays
        # why? because (a1 - b1) + (a2 - b2) is the same as (a1 + a2) - (b1 + b2)
        max_sum = sm(gt)
        min_sum = sm(lt)
        return max_sum - min_sum  