""" [搜索二维矩阵](https://www.lintcode.com/problem/search-a-2d-matrix/description?_from=ladder&&fromId=6)
写出一个高效的算法来搜索 m × n矩阵中的值。
这个矩阵具有以下特性：
每行中的整数从左到右是排序的。
每行的第一个数大于上一行的最后一个整数。
"""


class Solution:

    def searchMatrix(self, matrix: list, target: int) -> bool:
        """
        :param matrix: matrix, a list of lists of integers
        :param target: An integer
        :return: a boolean, indicate whether matrix contains target
        """
        if not (matrix and matrix[0]):
            return False
        m, n = len(matrix), len(matrix[0])
        top, bottom = 0, m - 1
        while top <= bottom:
            row_idx = top + ((bottom - top) >> 1)
            if matrix[row_idx][0] > target:
                bottom = row_idx - 1
            elif matrix[row_idx][n-1] < target:
                top = row_idx + 1
            else:
                row = matrix[row_idx]
                l, r = 0, n - 1
                while l <= r:
                    mid = l + ((r - l) >> 1)
                    if row[mid] == target:
                        return True
                    elif row[mid] > target:
                        r = mid - 1
                    else:
                        l = mid + 1
                # 这个break很关键, 否则在找不到目标值的情况下会进入死循环
                break
        return False
