class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left <= right:
            mid = (left + right) // 2

            sumh = sum(math.ceil(p / mid) for p in piles)
            
            if sumh > h:
                left = mid + 1
            else:
                right = mid - 1


        return left
        