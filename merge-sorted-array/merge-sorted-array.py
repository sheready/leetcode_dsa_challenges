class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        # get the last index of nums1
        last = m + n - 1 
        # merging in reverse order, comparing the length
        while m > 0 and n > 0:
            #to get the index of the element subtract 1 from the length.To compare the value of the element at index
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                #moving to the previous index of relevant elements of num1
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                #moving to the previous index of num2
                n -= 1

            #moving to the previous index of n+m-1 or num1
            last -= 1
        
        #fill nums1 with leftover nums2 elements 
        while n > 0:
            nums1[last] = nums2[n - 1]
            n = n - 1
            last = last - 1
        
        