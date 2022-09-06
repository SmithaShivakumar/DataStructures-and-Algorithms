class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        m = [[0 for i in range(c)] for j in range(r)]
        
        row=0
        col=0
        
        if (len(mat)*len(mat[0])) != (len(m)*len(m[0])):
            return mat
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                m[row][col] = mat[i][j]
                col += 1
                if col == c:
                    row += 1
                    col = 0
        print(m)
        return m