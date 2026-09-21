class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        len_inside = len(matrix[0]) # 2차원 배열 안에 있는 개별 리스트 크기 
        len_outside = len(matrix) # 2차원 배열의 원소수 

        top, down = 0, len_outside - 1
        left, right = 0, len_inside - 1
        target_row = -1

        while top <= down:
            mid = (top + down) // 2

            if matrix[mid][0] <= target <= matrix[mid][len_inside - 1]:
                target_row = mid
                break

            elif matrix[mid][len_inside - 1] > target:
                down = mid - 1
            
            elif matrix[mid][len_inside - 1] < target:
                top = mid + 1
            
        if target_row == -1:
            return False
            
            
        while left <= right:
            mid_col = (left + right) // 2

            if matrix[target_row][mid_col] == target:
                return True
            
            if matrix[target_row][mid_col] > target:
                right = mid_col - 1
            
            if matrix[target_row][mid_col] < target:
                left = mid_col + 1
            
        
        return False
 


        