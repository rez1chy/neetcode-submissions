class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #Count frequencies
        counts = Counter(nums)

        #Extract only the numbers (keys) of the top k elements
        top_k = [item for item, frequency in counts.most_common(k)]

        return(top_k)
