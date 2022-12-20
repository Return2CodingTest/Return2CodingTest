#102. Binary Tree Level Order Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = []
    def setResWithOrder(self, ord, root):
        if not root:
            return 
        if len(self.res) <= ord:
            self.res.append([root.val])
        else:
            self.res[ord].append(root.val)
        self.setResWithOrder(ord+1, root.left)
        self.setResWithOrder(ord+1, root.right)

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res = []
        self.setResWithOrder(0, root)
        return self.res
