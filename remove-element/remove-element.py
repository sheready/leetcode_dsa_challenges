class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        #initialize a pointer to the values that are not equal to val
        k = 0
        
        #iterate through the array
        
        for i in range(len(nums)):
            #find the index of the value that is not equal to val
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k