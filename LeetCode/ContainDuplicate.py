class Solution:
    def containDuplicate(self,nums):
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]== nums[j]:
                    return True;       
        return False;

    def containDuplicateSet(self,nums):
        uniqueset = set();# use set to store unique elements

        for i in nums:
           if i in uniqueset:
               return True;
        uniqueset.add(i);
        
        return False;
    
    def sortContainDuplicate(self,nums):
        nums.sort();

        for i in range(0,len(nums)):
            if nums[i]==nums[i+1]:
                return True;
        return False;

class Solution2:
    
    def containDuplicate2(self,nums)-> bool:
        for i in range(0,len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
    
    def containDuplicateset(self,nums):
        uniqueset2 = set()
        
        for i in nums:
             if i in uniqueset2:
                 return True
             uniqueset2.add(i)
        return False
                       
    def sortContainDuplicate(self,nums):
        nums.sort()
        
        for i in range(0,len(nums)):
            if nums[i]==nums[i+1]:
                return True
        return False
                            

if __name__ == '__main__':
    sol = Solution2()
    num = [1,2,3,4];
    print(sol.containDuplicate2(num));

    nums2 = [1,2,2,1];
    print(sol.containDuplicate2(nums2));