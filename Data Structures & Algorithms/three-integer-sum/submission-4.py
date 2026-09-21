class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        length = len(nums)

        for i in range(length):
            left, right = i + 1, length - 1

            if i >= 1 and nums[i] == nums[i-1]:
                continue 

            while left < right:
                k = nums[i]

                if nums[left] + nums[right] == -k:
                    result.append([k, nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif nums[left] + nums[right] < -k:
                    left += 1
                
                else:
                    right -= 1
        
        return result
            
                
                


        