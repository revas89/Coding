class Solution:
  def findNonDuplicate(self,arr):
    curr,next1 = 0,1
    while curr < len(arr):
      if arr[next1-1] != arr[curr]:
        arr[next1] = arr[curr]
        next1+=1     
      curr+=1      
    return arr

if __name__ == '__main__':
  s = Solution()
  result = s.findNonDuplicate([2, 3, 3, 3, 6, 9, 9])
  print(result)
  