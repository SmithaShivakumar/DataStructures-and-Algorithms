# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        leftPrev, cur = dummy, head
        for i in range(left -1):   # getting a dummy to connect to the left list node
            leftPrev, cur = cur, cur.next
            
        prev = None
        for i in range(right - left + 1): # reversing the middle order
            tempNxt = cur.next
            cur.next = prev
            prev, cur = cur, tempNxt
            
        leftPrev.next.next = cur #cur is the list node after right
        leftPrev.next = prev # prev is right list node
        
        return dummy.next