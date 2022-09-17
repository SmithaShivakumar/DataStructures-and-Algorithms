# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:       
        fastptr, slowptr = head, head        
        if (head is not None):
            while (fastptr is not None) and (fastptr.next is not None):
                fastptr = head.next.next
                slowptr = head.next
        return slowptr.next    '''
    
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        count = 0
        
        while head:
            # only update when count is odd
            if (count & 1):
                temp = temp.next
            head = head.next
            # increment count in each iteration
            count += 1

        print('temp.next',temp)
        return temp