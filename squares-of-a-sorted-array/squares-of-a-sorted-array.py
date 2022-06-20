class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sorted_list = map(lambda x:x**2,nums)
        sorted_list.sort()
        return sorted_list
    
obj1 = Solution()
print(obj1.sortedSquares([-7,-3,2,3,11]))
print(obj1.sortedSquares([-4,-1,0,3,10]))
        