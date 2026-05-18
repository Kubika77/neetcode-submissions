class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for idx, num in enumerate(nums):
            needed = target - num
            if needed in nums_dict:
                return [nums_dict[needed], idx]
            nums_dict[num] = idx
        return None