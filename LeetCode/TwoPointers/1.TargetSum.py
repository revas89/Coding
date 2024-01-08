class Solution:
  def search(self,targetsum,arr) -> list:
    resultlist = []
    first = 0
    last = len(arr)-1
    
    while first<=last:
      testresult = arr[first] + arr[last]
      if testresult == targetsum:
        resultlist.append(list([first, last]))
        first+=1
        last-=1
      elif testresult<targetsum:
        first+=1
      else:
        last-=1
    
    return resultlist
if __name__ == '__main__':
  s = Solution()
  result = s.search(8,[1,2,6,7])
  print(result)
  
      
        