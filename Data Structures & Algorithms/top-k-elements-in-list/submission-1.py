from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        out = []

        for num in nums:
            count[num] += 1
            
        sorted_c = dict(sorted(count.items(), key=lambda x: x[1]))

        return list(sorted_c.keys())[-k:]

        