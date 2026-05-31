class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}

        if len(s) != len(t):
            return False
        
     
        for char in s:
            if char in dict1:
                dict1[char] += 1
            else:
                dict1[char] = 1
        
        for char2 in t:
            if char2 in dict2:
                dict2[char2] += 1
            else:
                dict2[char2] = 1
        

        return dict1 == dict2