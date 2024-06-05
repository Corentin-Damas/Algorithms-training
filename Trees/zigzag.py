from typing import Optional, List
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return None

        q = [root]
        res = []
        zigZag = True

        while q:
            lenQ = len(q)
            acc = []

            for i in range(lenQ):
                poped = q.pop(0)
                if poped:
                    acc.append(poped.val)
                    q.append(poped.left)
                    q.append(poped.right)

            if acc:
                if not zigZag:
                    acc.reverse()
                    res.append(acc)
                else:
                    res.append(acc)
                    
            if zigZag == True:
                zigZag = False
            else:
                zigZag = True

        return res
