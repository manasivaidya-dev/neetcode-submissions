# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        head = prev
        return head
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or (head.next is None and n == 1):
            return None
        new_head = self.reverse(head)
        if n == 1:
            return self.reverse(new_head.next)
        curr = new_head 
        while n > 2:
            curr = curr.next
            n-=1
        if curr and curr.next:
            rmv = curr.next
            curr.next = rmv.next
            rmv.next = None
        answer_head = self.reverse(new_head)
        return answer_head
        
        