""" [二进制1的个数](https://www.lintcode.com/problem/count-1-in-binary/description?_from=ladder&&fromId=6)
计算在一个 32 位的整数的二进制表示中有多少个 1。
注意Python中负数的二进制的形式是取反;
"""


class Solution:
    def count_ones(self, n: int):
        if n == 0:
            return 0
        elif n < 0:
            n = 2 ** 32 + n
        count = 0
        while n > 0:
            count += 1
            n = n & (n - 1)
        return count
