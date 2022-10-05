class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #need to initialize max count
        #initialize count
        
        maxvalue = 0
        count = 0
       
    #iterate over the nums elements
        
        for i in range(len(nums)):
            #check if value at index is 1
            if nums[i] == 1:
                count = count + 1
                maxvalue = max(count,maxvalue)
            else:
                count=0
        return maxvalue      
        
        
            
        
        