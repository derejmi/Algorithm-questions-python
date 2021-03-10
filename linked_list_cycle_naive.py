# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        #we make an empty set using set()
        #while on != nukk
        #we traverse the list and for each node we check if the node is in 
        #the set
        #if it is in the set, we return True
        #if not in the set we save the node in the set
        #if we break out of the while loop return False
        
        nodes = set()
        on = head
        
        
        while on != None:
            if on in nodes:
                return True
            else:
                nodes.add(on)
                on = on.next
        
        return False