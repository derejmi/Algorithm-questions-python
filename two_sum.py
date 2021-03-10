class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        ht ={}
        
        for i, num in enumerate(nums):
            counterpart = target - num
            if counterpart in ht:
                return[i,ht[counterpart]]
            
            else:
                ht[num] = i
        
        
        