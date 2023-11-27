import math
class Solution:
  def makeSquares(self, arr):
    leftPointer = 0
    rightPointer = len(arr)-1;
    n = len(arr)
    resultArray = [0 for x in range(n)]
    resultPointer = len(arr)-1
    
    while leftPointer<=rightPointer:
        if abs(arr[leftPointer]) < abs(arr[rightPointer]):
            squared = arr[rightPointer]*arr[rightPointer]
            resultArray[resultPointer] = squared
            rightPointer-=1
            resultPointer-=1
        else:
            squared = arr[leftPointer]*arr[leftPointer]
            resultArray[resultPointer] = squared
            leftPointer+=1
            resultPointer-=1
    
    return resultArray  


def main():
    s = Solution()
    print(s.makeSquares([-3,-2,-1]))
    
main()
