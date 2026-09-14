class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited = []
        for num in nums:
            if num not in visited:
                visited.append(num)
                continue
            return True
        return False

        