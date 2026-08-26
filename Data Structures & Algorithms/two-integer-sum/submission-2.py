from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = defaultdict(int)
        for idx, num in enumerate(nums):
            expected = target - num
            if expected in seen:
                return [seen[expected], idx]
            seen[num] = idx
        