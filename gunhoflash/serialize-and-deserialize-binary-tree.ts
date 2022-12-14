class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;
  constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

TreeNode.prototype.toString = function () {
  return JSON.stringify({
    val: this.val,
    left: this.left,
    right: this.right,
  });
}

/*
 * Encodes a tree to a single string.
 */
function serialize(root: TreeNode | null): string {
  return JSON.stringify(root);
}

/*
 * Decodes your encoded data to tree.
 */
function deserialize(data: string): TreeNode | null {
  const node = JSON.parse(data) as TreeNode | null;
  return node && new TreeNode(
    node.val,
    node.left ? deserialize(JSON.stringify(node.left)) : null,
    node.right ? deserialize(JSON.stringify(node.right)) : null,
  );
}
