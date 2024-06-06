from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    res = float('inf')
    last = float('inf')

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        def searchMin(curr):
            if curr.left:
                searchMin(curr.left)

            self.res = min(self.res, abs(self.last - curr.val))
            self.last = curr.val

            if curr.right:
                searchMin(curr.right)

        searchMin(root)
        return self.res
