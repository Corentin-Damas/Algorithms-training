# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        res = []
        q = [root]

        while q:
            rightSide = None

            for i in range(len(q)):
                curr = q.pop(0)
                if curr:
                    rightSide = curr
                    q.append(curr.left)
                    q.append(curr.right)

            if rightSide:
                res.append(rightSide.val)
        return res
