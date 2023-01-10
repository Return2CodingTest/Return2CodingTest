/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */
var lowestCommonAncestor = function (root, p, q) {
  const min = Math.min(p.val, q.val);
  const max = Math.max(p.val, q.val);

  if (min <= root.val && max >= root.val) {
    return root;
  } else {
    return (
      (root.left && lowestCommonAncestor(root.left, p, q)) ||
      (root.right && lowestCommonAncestor(root.right, p, q))
    );
  }
};
