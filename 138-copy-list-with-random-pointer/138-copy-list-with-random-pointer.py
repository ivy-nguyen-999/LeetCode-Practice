"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = {}
        
        def clone(node):
            if node in hashmap:
                return hashmap[node]
            
            #base case:
            if node == None:
                return None
            
            copy = Node(node.val)
            hashmap[node] = copy
            # recursively find next value
            if node.next:
                copy.next = clone(node.next)
            # find next random
            copy.random = clone(node.random)
            return copy
        
        return clone(head)
        """
        hashmap = {}
        
        init = addVal = head
        
        while init:
            hashmap[init] = Node(init.val)
            init = init.next
            
        while addVal:
            hashmap[addVal].next = hashmap[addVal.next] if addVal.next else None
            hashmap[addVal].random = hashmap[addVal.random] if addVal.random else None
            addVal = addVal.next
            
        return hashmap[head] if head else None
        """