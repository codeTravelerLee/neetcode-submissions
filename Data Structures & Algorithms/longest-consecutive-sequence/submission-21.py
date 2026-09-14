class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()

        length = len(nums)

        maxlen = 1
        curlen = 1

        for i in range(1, length):
            if nums[i] == nums[i-1]:
                continue
            
            if nums[i] == nums[i-1] + 1:
                curlen += 1

            else:
                maxlen = max(maxlen, curlen)
                curlen = 1
        
        return max(curlen, maxlen)




        