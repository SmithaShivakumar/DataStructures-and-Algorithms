class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        mat = [[1]]
        
        for i in range(rowIndex):
            temp = [0] + mat[-1] + [0]
            row = []
            print('mat',mat[-1])
            print('temp',temp)
            for j in range(len(mat[-1])+1):
                row.append(temp[j]+temp[j+1])
            mat.append(row)
        return mat[rowIndex]