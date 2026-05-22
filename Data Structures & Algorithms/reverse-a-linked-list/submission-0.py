# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        else:
            current = head
            before = None
            after = current.next
            while current:
                after = current.next
                current.next = before
                before = current
                current = after
            head = before
            return head    
