from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)
        most_common = count.most_common(k)
        return [com[0] for com in most_common]
        