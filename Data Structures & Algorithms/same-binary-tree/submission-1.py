# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pList: list[Optional[int]] = []
        qList: list[Optional[int]] = []

        def dfs(node: Optional[TreeNode], output: list[Optional[int]]) -> None:
            
            if not node:
                output.append(None)
                return

            output.append(node.val)            
            dfs(node.left, output)
            dfs(node.right, output)
                   
        dfs(p, pList)
        dfs(q, qList)

        return pList == qList
        