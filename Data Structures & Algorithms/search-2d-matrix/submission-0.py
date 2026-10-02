class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        lr = 0
        rr = m - 1

        while lr <= rr:
            mid = (lr + rr) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                # check this row
                l = 0
                r = n - 1
                while l <= r:
                    m2 = (l+r)//2
                    val = matrix[mid][m2]
                    if val == target:
                        return True
                    elif val < target:
                        l = m2+1
                    else:
                        r=m2-1
                return False
            elif target < matrix[mid][-1]:
                rr = mid - 1
            else:
                lr = mid + 1
        return False
        