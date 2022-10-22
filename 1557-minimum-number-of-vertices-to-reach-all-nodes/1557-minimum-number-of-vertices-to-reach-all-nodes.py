class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        ans = set(range(n))
        #print('ans', ans)
        
        for e in edges:
            #print(e)
            if e[1] in ans:
                ans.remove(e[1])
        return list(ans)