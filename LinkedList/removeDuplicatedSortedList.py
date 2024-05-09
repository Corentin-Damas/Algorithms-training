# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy 
        while cur.next and cur.next.next: 
            if cur.next.val == cur.next.next.val:
                while cur.next and cur.next.next and cur.next.val == cur.next.next.val:
                    cur.next = cur.next.next

                cur.next = cur.next.next

            else:
                cur =  cur.next
        
        return dummy.next
                