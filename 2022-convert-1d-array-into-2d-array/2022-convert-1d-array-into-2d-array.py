class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        mat = []#[[0 for i in len(m)] for j in len(n)]
        itr = 0
        
        if (m*n) != len(original):
            return []
        # M iterations
        # Pick N elements each
        for i in range(1, m+1):
            array = []
            while itr < i*n:
                array.append(original[itr])
                itr += 1
            mat.append(array)
        print(mat)
        return mat