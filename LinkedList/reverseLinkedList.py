# Given the head of a singly linked list, reverse the list, and return the reversed list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

head = [1,2,3,4,5]
def reverseListIter(head: ListNode) -> ListNode:
    # Time O(n), Memory O(1)
    previous = None
    current = head
    
    while current:
        next = current.next # temp variable so we don't break entirely the NodeList when we reverse the pointer
        current.next = previous #reverse pointer instead of pointing forward we make it point to the previous data
        previous = current # shift poiter
        current = next
    return previous

        
def reverseListRec(head: ListNode) -> ListNode:
    # Time O(n), Memory O(n)
    if not head:
        return None
    
    newHead = head
    if head.next:
        newHead = reverseListRec(head.next)
        head.next.next = head
    head.next = None
    return newHead