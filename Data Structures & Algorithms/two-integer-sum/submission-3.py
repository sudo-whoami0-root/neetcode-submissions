class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {}
        

        for index, value in enumerate(nums):
            find = target - value
            if find in pairs:
                return [pairs[find], index]
            pairs[value] = index


        
        



    



        
    
    



        


