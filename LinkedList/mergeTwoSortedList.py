# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

def mergeTwoLists(list1, list2) -> ListNode:
    newNodelist = ListNode()
    tail = newNodelist      # we need to start with a "dummy Node list to init it"
    while list1 and list2:  # while list 1 and list 2 are none null
        if list1.val < list2.val:
            tail.next = list1
            list1 =list1.next # we update the pointer of the list1 
        else:                 # list1.val > list2.val:
            tail.next = list2
            list2 =list2.next
    if list1:   # if there is remaining node in list 1 and list 2 is empty, load all the remaining nodes in the newlist 
        tail.next = list1
    elif list2:
        tail.next = list2
    return newNodelist.next