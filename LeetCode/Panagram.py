
class Solution:

    def panagram(self,sentence)-> bool:
        pSet = set();

        for currChar in sentence.lower():
            if currChar.isalpha():
                pSet.add(currChar);
            
        return len(pSet)==26;
                
if __name__ == '__main__':
    sol = Solution();
    sentence = 'abcdefghijklmnopqrstuvwxyz';
    print(sol.panagram(sentence));