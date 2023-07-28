# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def hasCycle(head) -> bool:
    # speed : O(n) memory: O(n)
    memory: {}
    count : 0
    
    while head and head.next :
        if memory.get(head.next):
            return True,  memory[head.next]
        
        memory[head.next] = count 
        count +=1
    
    return False
    
        
# Other solution called Floyd's Tortoise & Hare that doesn't require momory
# Based on a 2 pointer technics where one is going fast and one slow 
# If the fast reach a Null meaning that there is no cycle, 
# but if they both get the same value that will mean there is a cycle

def hasCycleFloyds(head) -> bool:
    # speed: O(n)  memory: O(1)
    slow, fast = head, head
    
    while fast and fast.next :
        slow = slow.next # +1 node
        fast = fast.next.next # +2 node 
        if slow == fast:
            return True
    
    return False