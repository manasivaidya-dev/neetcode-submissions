# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reorder(h, t):
            curr_head = h
            curr_tail = t
            if curr_head == curr_tail:
                #odd case
                curr_head.next = None
                return
            elif curr_head.next == curr_tail:
                #even case
                curr_tail.next = None
                return
            next_head = curr_head.next
            next_tail = curr_head
            while next_tail.next != curr_tail:
                next_tail = next_tail.next
            curr_head.next = curr_tail
            curr_tail.next = next_head
            reorder(next_head, next_tail)

        tail = head
        while tail.next:
            tail = tail.next
        return reorder(head,tail)
        

        