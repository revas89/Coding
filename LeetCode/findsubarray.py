# Given an array with positive numbers and a positive target number, find all of its contiguous subarrays whose product is less than the target number.

# Example 1:

# Input: [2, 5, 3, 10], target=30                                              
# Output: [2], [5], [2, 5], [3], [5, 3], [10]                           
# Explanation: There are six contiguous subarrays whose product is less than the target.
# Example 2:

# Input: [8, 2, 6, 5], target=50                                              
# Output: [8], [2], [8, 2], [6], [2, 6], [5], [6, 5]                         
# Explanation: There are seven contiguous subarrays whose product is less than the target.

from collections import deque

class Solution:
  def findSubarrays(self, arr, target):
    resultArray = []
    windowstart, windowProduct = 0,1
    
    for windowend in range(len(arr)):
      windowProduct *= arr[windowend]
      
      while windowProduct >=target and windowstart<=windowend:
        windowProduct/=arr[windowstart]
        windowstart+=1
      
      tempArray = []  
      for i in range(windowend, windowstart-1,-1):
        tempArray.append(arr[i])
        resultArray.append(list(tempArray))
      
    return resultArray
  
def main():
        sol = Solution()
        result = sol.findSubarrays([8,2,6,5],30)
        print(str(result))

main()