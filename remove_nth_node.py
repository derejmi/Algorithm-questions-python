# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        #traverse LL - work out length 
        
        #edge case - if length = n - return head.nexr
        
        #work out index to be traversed up to - starting at 0
        
        #traverse the LL again up to index - 1
        
        # set using an on pointer the .next of the node at length -1 to on.next.next
        
        
        on = head
        length = 0
        
        while on != None:
            length += 1
            on = on.next 
        
        if length == n:
            return head.next
        
        left_index = length - n 
        
        on = head
        index = 0
        
        while index <= left_index - 1: 
            if index == left_index - 1:
                on.next = on.next.next
                return head
            on = on.next
            index += 1
            