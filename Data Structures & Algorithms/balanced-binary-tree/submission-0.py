# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def h(node: Optional[TreeNode]) -> tuple[bool, int]:
            if not node:
                return True, 0

            leftBalance, leftH = h(node.left)
            if not leftBalance:
                return False, 0

            rightBalance, rightH = h(node.right)
            if not rightBalance:
                return False, 0

            balanced = abs(rightH - leftH) <= 1
            height = 1 + max(leftH, rightH)

            return balanced, height
        
        isBalanced, _ = h(root)
        return isBalanced
        