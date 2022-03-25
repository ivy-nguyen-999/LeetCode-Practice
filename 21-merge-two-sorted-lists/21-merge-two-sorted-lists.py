# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if (list1 == None and list2 == None):
            return None
            
        node = ListNode()
        head = node
        
        while (list1 != None and list2 != None):
            
            if (list1.val <= list2.val):                    
                node.val = list1.val
                list1 = list1.next
            else:
                node.val = list2.val
                list2 = list2.next
            
            if (list1 != None or list2 != None):
                node.next = ListNode()
                node = node.next
        
        # left over elements
        while (list1 != None):
            node.val = list1.val
            list1 = list1.next
            if (list1 != None):
                node.next = ListNode()
                node = node.next
            
        while (list2 != None):
            node.val = list2.val
            list2 = list2.next
            if (list2 != None):
                node.next = ListNode()
                node = node.next
        
        return head