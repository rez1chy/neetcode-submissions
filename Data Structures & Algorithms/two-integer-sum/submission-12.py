class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #will the list be sorted?

        #start with the lowest (first) number and add the rest with it
        #if target is achieved we can conclude
        #else move to the next and add other in list (forget the seen list a they are already checked)

        # visited_index = []

        for i in range(len(nums)):
            print(f'I={i}')
            for j in range(i+1, len(nums)):
                print(f'J={j}')

                if i == j:
                    j+=1
                    print(f'J+1 ={j}')
                elif i >= len(nums):
                    return
                elif nums[i] + nums[j] == target:
                    return [i, j]
                # else:
                #     visited_index.append(i)
                #     visited_index.append(i+j)
