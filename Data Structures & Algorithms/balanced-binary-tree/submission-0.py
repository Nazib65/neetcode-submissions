# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def bal(node):
            if not node:
                return True, 0
            leftBal, leftHeight=bal(node.left)
            rightBal, rightHeight=bal(node.right)
            balanced= leftBal and rightBal and abs(leftHeight-rightHeight)<=1
            height=max(leftHeight, rightHeight)+1
            return balanced, height
        return bal(root)[0]