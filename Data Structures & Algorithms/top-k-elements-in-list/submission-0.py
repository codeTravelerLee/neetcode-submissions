class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_hash = defaultdict(int)

        for num in nums:
            my_hash[num] += 1
        
        result = sorted(my_hash.items(), key = lambda x: x[1], reverse=True)
        return [item[0] for item in result[:k]]
        