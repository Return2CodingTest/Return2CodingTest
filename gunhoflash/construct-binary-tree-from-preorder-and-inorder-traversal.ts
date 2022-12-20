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

function buildTree(preorder: number[], inorder: number[]): TreeNode | null {
  if (preorder.length === 0) return null;

  const val = preorder[0];
  const indexOfValInInorder = inorder.findIndex(v => v === val);

  const leftPreorder = preorder.slice(1, 1 + indexOfValInInorder);
  const leftInorder = inorder.slice(0, indexOfValInInorder);
  const leftNode = buildTree(leftPreorder, leftInorder);

  const rightPreorder = preorder.slice(1 + indexOfValInInorder);
  const rightInorder = inorder.slice(indexOfValInInorder + 1);
  const rightNode = buildTree(rightPreorder, rightInorder);

  const node = new TreeNode(val, leftNode, rightNode);
  return node;
}
