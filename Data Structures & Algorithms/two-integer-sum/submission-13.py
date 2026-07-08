class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #will the list be sorted?

        #start with the lowest (first) number and add the rest with it
        #if target is achieved we can conclude
        #else move to the next and add other in list (forget the seen list a they are already checked)

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]