class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {}
        out = []

        for index, value in enumerate(nums):
            pairs[value] = index


        for i in range(len(nums)):
            find = target - nums[i]
            if find in pairs and pairs[find] != i:
                out.append(i)
                out.append(pairs[find])
                return out

        return 

            
        
        



    



        
    
    



        


