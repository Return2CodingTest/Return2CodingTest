
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def cloneGraph(node: Node) -> Node:
    nodeToNeighbor = {}
    nodeToRef = {}
    
    def destructNode(n: 'Node'):
        if not n.val in nodeToNeighbor:
            nodeToNeighbor[n.val] = []
            for neighbor in n.neighbors:
                nodeToNeighbor[n.val].append(neighbor.val)
                destructNode(neighbor)
        
    destructNode(node)
    for n in nodeToNeighbor:
        ref = Node(n)
        nodeToRef[n] = ref
    
    for n in nodeToRef:
        nodeToRef[n].neighbors = [nodeToRef[neighbor] for neighbor in nodeToRef[n].neighbors]
    
    return nodeToRef[1]

print(cloneGraph)

#unsolved