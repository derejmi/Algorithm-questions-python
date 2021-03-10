# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        #set prev initially to None
        #set an on pointer to the head provided as an argument
        #while on != None:
          #temp = on.next
          #on.next = prev
          #prev = on
          #on = temp
        #return prev
        
        
        prev = None
        on = head
        
        while on != None:
            temp = on.next
            on.next = prev
            prev = on
            on = temp
        return prev
    