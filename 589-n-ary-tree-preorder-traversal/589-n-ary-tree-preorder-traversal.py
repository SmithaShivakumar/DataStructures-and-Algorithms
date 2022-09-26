"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        q = deque([root])
        output = []
        
        while q:
            cand = q.popleft()
            output.append(cand.val)
            for c in reversed(cand.children):
                q.appendleft(c)
                
        return output