# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def merge2lists(self, one: Optional[ListNode], two:Optional[ListNode]) -> Optional[ListNode]:
        start = ListNode(0, None)
        first = one
        second = two
        prev = start
        while first and second:
            if first.val < second.val:
                prev.next = first
                prev = first
                first = first.next
            else:  
                prev.next = second
                prev = second
                second = second.next
        if first:
            prev.next = first
        elif second:
            prev.next = second
        return start.next
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if n== 1:
            return lists[0]
        elif n == 0:
            return None
        
        mid = n //2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])

        return self.merge2lists(left,right)
        
            



        