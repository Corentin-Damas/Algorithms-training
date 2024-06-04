from typing import Optional, List
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q= [root]
        res = []
        
        while q:
            lenQ = len(q)
            lvl = []
            
            for i in range(lenQ):
                poped = q.pop(0)
                
                if poped:
                    lvl.append(poped.val)
                    q.append(poped.left)
                    q.append(poped.right)
            if lvl:
                res.append(lvl)
        return res
        
        
