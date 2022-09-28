from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        count = Counter(s)
        for c in count.values():
            ans += (c // 2) * 2
            if ans % 2 == 0 and c % 2 == 1:
                ans += 1
        return ans
        