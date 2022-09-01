class Node:
  def __init__(self, val = 0, neighbors = None):
    self.val = val
    self.neighbors = neighbors if neighbors is not None else []

class Solution:
  def cloneGraph(self, node: Node) -> Node:
    clones = [Node(i) for i in range(101)]
    isVisited = [False] * 101

    if node is None:
      return None

    visitingStack = [node]
    while len(visitingStack):
      now = visitingStack.pop()

      if isVisited[now.val]: continue
      isVisited[now.val] = True

      for neighbor in now.neighbors:
        if not isVisited[neighbor.val]:
          clones[now.val].neighbors.append(clones[neighbor.val])
          clones[neighbor.val].neighbors.append(clones[now.val])
          visitingStack.append(neighbor)

    return clones[node.val]
