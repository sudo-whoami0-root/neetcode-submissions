from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ang1 = defaultdict(int)
        ang2 = defaultdict(int)

        if len(s) != len(t):
            return False

        for char in s:
            ang1[char] += 1
        
        for char in t:
            ang2[char] += 1

        return ang1 == ang2

        