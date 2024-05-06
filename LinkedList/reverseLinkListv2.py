
from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        # reach node at position  'left'
        leftPrev, curr = dummy, head
        for i in range(left - 1):
            leftPrev, curr = curr, curr.next

        # curr='left', leftPref = "node beofre left"
        # reverse from left to right
        prev = None
        for i in range(right - left + 1):
            tmpNext = curr.next
            curr.next = prev
            prev, curr = curr, tmpNext

        # update pointers
        leftPrev.next.next = curr # curr is node after "right"
        leftPrev.next = prev      #prev is "right"
        
        return dummy.next