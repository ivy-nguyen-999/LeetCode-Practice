# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        currentNode = ListNode()
        head = currentNode
        # stop when one or both lists are empty
        while(l1 is not None and l2 is not None):
            # calculate the value
            adding = l1.val + l2.val + currentNode.val
            currentNode.val = adding % 10
            # move to next nodes for l1, l2
            l1, l2 = l1.next, l2.next
            # if l1 or l2 is not none
            if(adding >= 10 or l1 is not None or l2 is not None):
                # to carry over to the next digit, either 1 or 0
                addend = adding >= 10 and 1 or 0
                currentNode.next = ListNode(addend)
                currentNode = currentNode.next
            
        while(l2 is not None):
            # calculate the value
            adding = l2.val + currentNode.val
            currentNode.val = adding % 10
            # move to next nodes for l2
            l2 = l2.next
            # if l2 is not none
            if(adding >= 10 or l2 is not None):
                # to carry over to the next digit, either 1 or 0
                addend = adding >= 10 and 1 or 0
                currentNode.next = ListNode(addend)
                currentNode = currentNode.next
        while(l1 is not None):
            # calculate the value
            adding = l1.val + currentNode.val
            currentNode.val = adding % 10
            # move to next nodes for l1
            l1 = l1.next
            # if l1 is not none
            if(adding >= 10 or l1 is not None):
                # to carry over to the next digit, either 1 or 0
                addend = adding >= 10 and 1 or 0
                currentNode.next = ListNode(addend)
                currentNode = currentNode.next
            
        return head
                
        