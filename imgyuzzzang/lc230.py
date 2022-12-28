# 230. Kth Smallest Element in a BST
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        valueList = []
        
        def readTree(root):
            if not root:
                return
            
            valueList.append(root.val)
            readTree(root.right)
            readTree(root.left)
        
        readTree(root)
        valueList.sort()
        
        return valueList[k-1]
    