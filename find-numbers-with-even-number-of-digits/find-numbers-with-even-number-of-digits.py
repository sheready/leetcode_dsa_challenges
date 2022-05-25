class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #iterate array
        #iterate the len of array elements
        
        count = 0
        
        #create a new array and stringify the elements iterated
        arr2 = map(str,nums)
        for x in arr2:
            
            if len(x) % 2 == 0:
                count += 1
        
            else:
                count +=0
        return count
obj1 = Solution()

print(obj1.findNumbers([12,345,2,6,7896]))
print(obj1.findNumbers([555,901,482,1771]))
            
        
                
                
        
        
        