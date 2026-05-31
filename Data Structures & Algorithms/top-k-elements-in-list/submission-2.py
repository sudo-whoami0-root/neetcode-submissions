from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        out = []

        freq = []
        for n in range(len(nums) + 1):
            freq.append([])
        
        for num in nums:
            count[num] += 1

        for key, value in count.items():
            freq[value].append(key)
        
        out = []
        for i in range(len(freq) -1, 0, -1):
            for n in freq[i]:
                out.append(n)
                if len(out) == k:
                    return out


            

        