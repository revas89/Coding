import re
class Solution:
    def isPalindrome(self, testStr: str) -> bool:
        testStr = re.sub("[^A-Za-z0-9]","",testStr).lower();
        print(testStr);
        array = list(testStr.lower());
        print(array);
        start = 0
        end = len(testStr)-1;
        
        if(len(array)) == 0:
            return False;
        
        while(end>=start):
            if array[start]==array[end]:
                start+=1;
                end-=1;
            else:
                return False;
            
        return True;   
    def isPalindrome2(self,teststr):
        teststr = "".join(c for c in teststr.lower() if c.isalpha())
        print(teststr)
        first = 0
        last = len(teststr)-1
        while first<=last :
            if teststr[first]!=teststr[last]:
                return False
            first+=1
            last-=1
        
        return True
            
        
        
                  
if __name__ == '__main__':
    s = Solution();
    print(s.isPalindrome2("A man, a plan, a canal, Panama!"))        
         
    