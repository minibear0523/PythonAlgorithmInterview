""" [斐波那契数列](https://www.lintcode.com/problem/fibonacci/description?_from=ladder&&fromId=6)
查找斐波纳契数列中第 N 个数。
所谓的斐波纳契数列是指：
前2个数是 0 和 1 。
第 i 个数是第 i-1 个数和第i-2 个数的和。
斐波纳契数列的前10个数字是：
0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ...
"""


class Solution:
    def fibonacci(self, n):
        """ 自顶向下使用记忆迭代的方式计算, 时间复杂度为 O(n)
        :param n:
        :return:
        """
        if n == 1:
            return 0
        elif n == 2:
            return 1
        x, y = 0, 1
        for i in range(3, n + 1):
            x, y = y, x + y
        return y

    def fibonacci2(self, n):
        """ 使用通项公式法, 该方法有误差, 误差随着 n 的增加而增加, 如果在误差允许的范围内, 该算法的复杂度为 O(logn), 因为计算 n 次方的复杂度为 logN
        :param n:
        :return:
        """
        from math import sqrt
        s = sqrt(5)
        return int(1 / s * (((1 + s) / 2) ** n) - ((1 - s) // 2) ** n)
