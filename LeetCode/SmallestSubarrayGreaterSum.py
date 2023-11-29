import math

class Solution:
  import math

class Solution:
  def findMinSubArray(self, s, arr):
    resultingArray = []
    finalArray = []
    windowstart,windowsum =0,0
    for windowend in range(len(arr)):
        windowsum+=arr[windowend]
        finalArray.append(arr[windowend])
          
        while windowsum >= s:
            resultingArray.append(list(finalArray))
            finalArray.remove(arr[windowstart])
            windowsum-=arr[windowstart]
            windowstart+=1
      
    if not resultingArray:
        return 0
    else:
        #return len(min((resultingArray),key=lambda x:len(x))) 
        return resultingArray   

def main():
    s = Solution()
    print(s.findMinSubArray(7,[2, 1, 5, 2, 8]))
    
main()