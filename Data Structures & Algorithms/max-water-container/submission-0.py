class Solution:
    def maxArea(self, heights: List[int]) -> int:
        length = len(heights)
        left, right = 0, length - 1
        max_size = 0

        while left < right:
            size = (right - left) * min(heights[left], heights[right])
            max_size = max(size, max_size)

            if heights[left] < heights[right]:
                left += 1
            
            else:
                right -= 1
        
        return max_size
            


# size = (right - left) * min(heights[left], heights[right])
        