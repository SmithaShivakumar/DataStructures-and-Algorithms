class Solution:    
    def partitionArray(self, A, k):
        A.sort()
        res, j = 1, 0
        for i in range(len(A)):
             if A[i] - A[j] > k:
                res += 1
                j = i
        return res
    
    
'''    def partitionArray(self, A, k):
        A.sort()
        res = 1
        mn = mx = A[0]
        for a in A:
            mn = min(mn, a)
            mx = max(mx, a)
            if mx - mn > k:
                res += 1
                mn = mx = a
        return res'''