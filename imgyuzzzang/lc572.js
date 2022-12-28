//572. Subtree of Another Tree

const isSubtree = (root, subRoot) => {
  if (!root) {
    return false;
  }

  if (JSON.stringify(root) === JSON.stringify(subRoot)) {
    return true;
  }

  return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
};
