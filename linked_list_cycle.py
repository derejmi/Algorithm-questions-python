# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        #we have a slow and fast pointer
        #on = head
        #fast = on
        #slow = on
        
        #while fast != None
            #if fast.next:
                #fast = on.next.next
                #slow = on.next
            #else return False
            #if fast == slow -> return True
            
        #return False
        
        fast = head
        slow = head
        
        while fast != None:
            if fast.next:
                fast = fast.next.next
                slow = slow.next
            else: return False
            if fast == slow:
                return True
            
        return False