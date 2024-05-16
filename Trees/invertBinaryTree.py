from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root: TreeNode) -> TreeNode:
    # Recursive definition, invert the 2 child of a node a do it for all nodes

    # Base case, no childrens
    if not root:
        return None

    # swap the children
    tmp = root.left
    root.left = root.right
    root.right = tmp

    # recursion will do the same as above for all and return when no root
    invertTree(root.left)
    invertTree(root.right)

    return root  # when finished


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        tmp = root.left
        root.left = root.right
        root.right = tmp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root