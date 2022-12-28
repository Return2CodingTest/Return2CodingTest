/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isValidBST = function (root, min = 2147483649, max = -2147483649) {
  if (!root) return true;
  if (root.left) {
    if (root.left.val >= root.val) return false;
    if (root.left.val <= max) return false;
  }
  if (root.right) {
    if (root.right.val <= root.val) return false;
    if (root.right.val >= min) return false;
  }
  return (
    isValidBST(root.left, Math.min(root.val, min), max) &&
    isValidBST(root.right, min, Math.max(root.val, max))
  );
};
