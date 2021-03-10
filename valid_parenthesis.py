class Solution:
    def isValid(self, s: str) -> bool:
        
        #have a hashtable which has the opening parenthesis as keys and the closing as values
        #loop over the string 
            #if string in ht - add opening p to stack
            #else compare string to the last parenthesis in the stack (pop off the stack) - i.e. if ht[lp] == str:
                    #if they are not equal return false
            
        #after the loop check if the stack still has a length if it does - return False
        #return True
            
        
        hashtable = {"{":"}","[":"]","(":")"}
        stack = []
        
        for str in s:
            if str in hashtable:
                stack.append(str)
            else:
                if len(stack) > 0:
                    open = stack.pop()
                    if hashtable[open] != str:
                        return False
                else:
                    return False
            
        if len(stack) > 0:
            return False
        
        return True
                