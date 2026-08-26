# from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sort_list = sorted(nums)
        longest = 0
        current = 1
        for idx, num in enumerate(sort_list):
            if idx < (len(sort_list) - 1) and sort_list[idx + 1] == num + 1:
                current += 1
                continue
            if idx < (len(sort_list) - 1) and sort_list[idx + 1] == num:
                continue
            longest = max(current, longest)
            current = 1
            continue
        return longest

