# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        result = [0]
        
        def dfs(root):
            if not root: 
                return -1   # -1 for the recursion to compensate the fact that we alway count + 2
                            # to count left and right at the same time but if it's empty we don't wanna count it
            
            left = dfs(root.left)
            right = dfs(root.right)
            result[0] = max(result[0], 2 + left + right) # Check for the max value during the recursion the first node is not always the biggest
            
            return 1 + max(left, right) 
    
        dfs(root)
        return result[0]