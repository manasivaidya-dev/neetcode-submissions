# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return
        elif not list1:
            return list2
        elif not list2:
            return list1
            
        l1 = list1
        l2 = list2
        if l1.val >= l2.val:
            head = l2
            l2 = l2.next
        else:
            head = l1
            l1=l1.next
        curr = head

        while l1 and l2:
            if l1.val >= l2.val:
                curr.next = l2
                l2 = l2.next
            else:
                curr.next = l1
                l1=l1.next
            curr = curr.next
        if not l1:
            curr.next = l2
        elif not l2:
            curr.next = l1
        return head

            #one list ends?


        