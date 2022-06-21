class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        # Initialize the length of array and index
        y = len(arr)
        i = 0
        while(i<len(arr)):
            if arr[i] == 0:
                i = i + 1
                arr.insert(i, 0)
            i = i+1
        diff = len(arr) - y
        for i in range(0, diff):
            arr.pop()

obj1 = Solution()
print(obj1.duplicateZeros([1,0,0,2,3,0,0,4]))

print(obj1.duplicateZeros([1,2,3]))