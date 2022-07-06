class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #This solution is being solved by comparing the left value to the right value, such that if it's unique the right value takes up the index of the left value.
        #https://youtu.be/DEJAZBq0FDA
        
        #initialize the left value by 1; this is because we assume that the firsindex at ) will always be a unique value
        left = 1;
        
        #iterate through the right values of the array from the 2nd value which is at index 1
        
        for right in range(1, len(nums)):
            if nums[right] != nums[right - 1]:
                nums[left] = nums[right]
                left += 1

        return left
       
  
                
          
            
            
        