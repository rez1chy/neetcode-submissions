class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_numbers = list(set(nums))
        if len(nums) != len(unique_numbers):
            return True
        else:
            return False