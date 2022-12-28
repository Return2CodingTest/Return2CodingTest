import sys

class TreeNode:
  def __init__(self, val = 0, left = None, right = None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def checkBST(self, root: Optional[TreeNode], minVal: int, maxVal: int) -> bool:
    if root is None: return True
    if root.val <= minVal or root.val >= maxVal: return False
    return self.checkBST(root.left, minVal, root.val) and self.checkBST(root.right, root.val, maxVal)

  def isValidBST(self, root: Optional[TreeNode]) -> bool:
    return self.checkBST(root, float('-inf'), float('inf'))
