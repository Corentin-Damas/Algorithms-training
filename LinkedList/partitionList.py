# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left, right = ListNode(), ListNode()
        lTail, rTail = left , right
        
        while head: 
            if head.val < x:
                lTail.next = head
                lTail = lTail.next
            else: 
                rTail.next = head
                rTail = rTail.next
                
            head = head.next
        
        lTail.next = right.next
        rTail.next = None
        return left.next
                
                