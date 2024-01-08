# Given a string sentence containing English letters (lower- or upper-case), return true if sentence is a Pangram, or false otherwise.

# A Pangram is a sentence where every letter of the English alphabet appears at least once.

# Note: The given sentence might contain other characters like digits or spaces, your solution should handle these too.

# Example 1:

# Input: sentence = "TheQuickBrownFoxJumpsOverTheLazyDog"
# Output: true
# Explanation: The sentence contains at least one occurrence of every letter of the English alphabet either in lower or upper case.
class Solution:
    def isPangram(self,str) -> bool:
        lowerstring = str.lower()
        alphabetset = set()
        
        for currChat in lowerstring:
            if currChat.isalpha():
                alphabetset.add(currChat)
        
        if len(alphabetset) == 26:
            return True
        
        return False
        
if __name__ == '__main__':
    s = Solution()
    print(s.isPangram("TheQuickBrownFoxJumpsOverTheLazyDog1234"))     
            
            
        
        