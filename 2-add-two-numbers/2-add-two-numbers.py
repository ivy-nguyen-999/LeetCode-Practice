# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # if l1 is empty
        if(l1 is None):
            return l2
        # let the head be l1
        head = l1
        addend = 0
        # stop looping if both lists are empty
        while(l1 or l2):
            # if there is l2 is empty and there is no addend
            if(l2 is None and addend == 0):
                break
            # calculate the current value
            l2Val = l2 and l2.val or 0
            tempVal = l1.val + l2Val + addend
            # new addend value
            addend = tempVal >= 10 and 1 or 0
            # add two numbers
            l1.val = tempVal % 10
            # all cases:
            # if next value in l1 is none
            # and l2 is not none
            if(l1.next is None and l2):
                l1.next, l2 = l2.next, None
            # or addend is not 0
            if(l1.next is None and addend == 1):
                l1.next = ListNode(addend)
                break
            # if next value in l1 is not none
            l1 = l1.next
            if(l2 is not None):
                l2 = l2.next
        
        return head
        