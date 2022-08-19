class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        #initialize pointer i at 0
        #loop through the array length
        # check if item at index is double any other item in the array
        
        x = 0
     
   
        for i in range(len(arr)):
            z = arr[i] * 2
            while x < len(arr):
                if(z == arr[x] and i != x):
                    return True
                x += 1
            x = 0   
        return False
             
       

               

           

            

            
     
            