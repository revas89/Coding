class Solution:    
      def findMaxSumSubArray(self,k, arr):
        maxSum = 0
        arrsum = 0
        windowstart = 0
        for windowend in range(len(arr)):
          arrsum+=arr[windowend]
        
          if windowend>=k-1:
            maxSum = max(arrsum,maxSum)
            arrsum-=arr[windowstart]
            windowstart+=1
        
        return maxSum
           
    
def main():
        sol = Solution()
        result = sol.findMaxSumSubArray(1, [1, 2, 3, 4, 5])
        print(str(result))

main()