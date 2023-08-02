# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepthRecursive(root: TreeNode) -> int:
    # Recursive DFS Depth First Search
    # Memory and Speed of 0(n)
    if not root: 
        return 0
    return 1 + max(maxDepthRecursive(root.left), maxDepthRecursive(root.right))

def maxDepthBFS(root: TreeNode) -> int:
    # Breadth-first search (we are going lvl by lvl not going to the root first, vertical way of seing)
    # Memory and Speed of 0(n)
    
    # We are using a queue were we had the node and look at it to solve it, we solve it by remove it and change it for his children if they exist 
    # Then at some point they will be no more childrens so we will stop the queue
    
    if not root:
        return 0
    
    level = 0
    q = deque([root])
    while q: 
        for i in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
                
        level +=1
    return level

def maxDepthIterative(root: TreeNode) -> int:
    # Call stack we put the node from the top on the top of the stack process it (remove it from the stack)
    # and add his childrens if he has some. 
    # Memory and Speed of 0(n)
    
    if not root: 
        return 0
    
    stack = [[root, 1]]
    result = 1
    while stack: 
        node, depth = stack.pop()
        
        if node:  # ignore null nodes
            result = max(result, depth) #update the result if we found a higher depth in the stack
            stack.extend([node.left, depth + 1])
            stack.extend([node.right, depth + 1])
    return result