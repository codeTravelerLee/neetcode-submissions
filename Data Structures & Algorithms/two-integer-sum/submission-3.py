class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        length = len(nums)

        for i in range(length):
            diff = target - nums[i]
            if diff in hashmap:
                return [hashmap[diff],i]
            hashmap[nums[i]] = i
        
        return []
            

        