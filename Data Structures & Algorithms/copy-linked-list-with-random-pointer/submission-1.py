"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        curr = head
        while curr:
            node = Node(curr.val)
            node.next = curr.next
            curr.next = node
            curr = curr.next.next
        #make randowm pointers point right
        new_curr = head
        while new_curr:
            copycurr = new_curr.next
            if new_curr.random:
                random = new_curr.random
                copyrandom = random.next
                copycurr.random = copyrandom
            if new_curr.random == None:
                copycurr.random = None
            new_curr = new_curr.next.next
        #detangle
        detangle = head
        new_head = head.next
        while detangle:
            if detangle.next:
                copied = detangle.next
                if copied.next:
                    next_detangle = copied.next
                    detangle.next = next_detangle
                    copied.next = next_detangle.next
                if copied.next == None:
                    detangle.next = None
                detangle = detangle.next
        return new_head



        