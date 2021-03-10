class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        #sort input nums
        #create an output array
        #do a for loop looping through numbers
        #set left = i + 1 and right as len(nums) - 1
        #if num[i] == nums[i-1] continue
        #while left < right
        #if nums[i] + nums[left] + nums right == 0
             #add to out put array
             #push through duplicates
        #if nums[i] + nums[left] + nums[right] < 0
             #left += 1
        #if nums[i] + nums[left] + nums[right] < 0
             #right -= 1
            
            nums.sort()
            output = []
            
            for i, num in enumerate(nums):
                left = i + 1
                right = len(nums) -1
                if i > 0 and nums[i] == nums[i-1]:
                    continue 
                
                while left < right:
                    total = nums[i] + nums[left] + nums[right]
                    if total == 0:
                        output.append([nums[i],nums[left],nums[right]])
                        while left < right and nums[left + 1] == nums[left]:
                            left += 1
                        while left < right and nums[right - 1 ] == nums[right]:
                            right -=1
                        left += 1
                        right -= 1
                        
                    if total < 0:
                        left += 1
                    if total > 0:
                        right -= 1
                        
            return output
                        
                        
                            
                    