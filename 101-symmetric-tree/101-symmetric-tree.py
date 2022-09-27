# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        return self.ismirror(root.left, root.right)
    
    def ismirror(self, leftroot, rightroot):
        if leftroot and rightroot:
            return (leftroot.val == rightroot.val and 
        self.ismirror(leftroot.right, rightroot.left) and
        self.ismirror(leftroot.left, rightroot.right))
        
        return leftroot == rightroot        