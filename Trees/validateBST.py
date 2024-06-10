from typing import Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:


        def req(cur, lBound, rBound):

            if not cur:
                return True

            if not (cur.val < rBound and cur.val > lBound):
                return False

            return (req(cur.left, lBound, cur.val) and req(cur.right, cur.val, rBound))

        return req(root, float('-inf'), float('inf'))

        # traverse left

        #  check prev

        # traverse right
