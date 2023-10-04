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
            
if __name__ == '__main__':
    s = Solution();
    print(s.isPalindrome("A man, a plan, a canal, Panama!"))        
         
    