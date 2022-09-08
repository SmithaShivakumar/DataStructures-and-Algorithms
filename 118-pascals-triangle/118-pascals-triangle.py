class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        mat = [[1]]
        print('mat_first',mat)    
        for i in range(0, numRows-1):
            temp = [0] + mat[-1] + [0] 
            row = []
            for j in range(len(mat[-1])+1):
                row.append(temp[j]+temp[j+1])
            mat.append(row)
        print('mat_final',mat)
        return mat