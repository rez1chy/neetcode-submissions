class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # #Count frequencies
        # counts = Counter(nums)

        # #Extract only the numbers (keys) of the top k elements
        # top_k = [item for item, frequency in counts.most_common(k)]

        # return(top_k)

        # 1. Count frequencies using a native dictionary
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        # 2. Create buckets where index = frequency. 
        # Max possible frequency is the length of nums.
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in counts.items():
            buckets[freq].append(num)
        
        # 3. Gather the top k elements starting from the highest frequency bucket
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
