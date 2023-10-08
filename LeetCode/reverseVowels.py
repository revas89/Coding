class Solution:
  def reverseVowels(self, s: str) -> str:
    # TODO: Write your code here
    count = 0;
    a = list(s);
    for i in range(0,len(a)):
        if s[i] in ('a','e','i','o','u','A','E','I','O','U'):
            count+=1;
    if count == 1:
        return s;
    i = len(a)-1;
    j =0;        
    while(count>0):
        while a[i] not in ('a','e','i','o','u','A','E','I','O','U'):
            i-=1;
        while a[j] not in ('a','e','i','o','u','A','E','I','O','U'):
            j+=1;
        swap = a[i];
        a[i] = a[j];
        a[j] = swap;
        i-=1;
        j+=1; 
        count-=2;
    return "".join();

if __name__ == '__main__':
    s = Solution();
    print(s.reverseVowels('REVA'));
    print(s.reverseVowels('AEIOU'));
    print(s.reverseVowels('DesignGUrus'));
    print(s.reverseVowels('Hello'));
    