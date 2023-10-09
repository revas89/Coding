class Solution:
    def maxSubarraySum(self,k,array) -> int:
        maxSum = 0
        if k > len(array):
            return 0;
        
        for i in range(len(array)-k+1):
            sum=0
            for j in range(i,i+k):
                sum+=array[j]
            
            if sum>maxSum:
                maxSum = sum            
        
        return maxSum             
    
def main():
        sol = Solution()
        result = sol.maxSubarraySum(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
        print("Averages of subarrays of size K: " + str(result))

main()