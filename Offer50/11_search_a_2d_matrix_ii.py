""" [搜索二维矩阵II](https://www.lintcode.com/problem/search-a-2d-matrix-ii/description?_from=ladder&&fromId=6)
写出一个高效的算法来搜索m×n矩阵中的值，返回这个值出现的次数。 这个矩阵具有以下特性：
每行中的整数从左到右是排序的。
每一列的整数从上到下是排序的。
在每一行或每一列中没有重复的整数。

这里与第10题的区别是, 并没有限制每一行最后的一个元素小于下一行的第一个元素.
"""


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :param matrix: A list of lists of integers
        :param target: An integer you want to search in matrix
        :return: An integer indicate the total occurrence of target in the given matrix
        """
        if not (matrix and matrix[0]):
            return 0
        m, n = len(matrix), len(matrix[0])
        r, c = m - 1, 0
        res = set()
        while 0 <= r < m and 0 <= c < n:
            if matrix[r][c] == target:
                res.add((r, c))
                r, c = r - 1, c + 1
            elif matrix[r][c] > target:
                r -= 1
            else:
                c += 1
        return len(res)