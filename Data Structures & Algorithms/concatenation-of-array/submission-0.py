class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_nums = nums.copy()
        nums.extend(new_nums)
        return nums
        