class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check = {}

        for value in nums:
            if value in check:
                return True
            else:
                check[value] = 1;
        return False

        
        


        