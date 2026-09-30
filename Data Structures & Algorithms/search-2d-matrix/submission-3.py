class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        low = 0
        high = m*n - 1
        # m*n elements
        #4*4  13 
        while low <= high:
            mid = (low + high)//2
            col = (mid % n)
            row = (mid // n)
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False


        