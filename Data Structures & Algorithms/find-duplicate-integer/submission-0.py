class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        countMap = dict()

        for num in nums:
            if num in countMap:
                countMap[num] += 1
            else:
                countMap[num] = 1

        dup = next(filter(lambda index: countMap[index] > 1, countMap))
        return dup


        
        