"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        hashmap = {} #to keep track which copied nodes
        
        def clone(node):
            if node in hashmap:
                #return its clone
                return hashmap[node]
            copy = Node(node.val)
            #add the copied node to hashmap
            hashmap[node] = copy
            #add its neighbor
            for neighbor in node.neighbors:
                copy.neighbors.append(clone(neighbor))
            return copy
        
        #in case the node doesn't have any neighbors
        return clone(node) if node else None