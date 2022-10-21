# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if root is None:
            return []
        
        rightSide = []
        nextLevel = deque([root,])
        
        
        while nextLevel:
            # prepare for next level
            currLevel = nextLevel
            nextLevel = deque()
            
            while currLevel:
                node = currLevel.popleft()
                
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
                
            rightSide.append(node.val) 
        
        return rightSide