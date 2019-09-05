""" [FizzBuzz问题](https://www.lintcode.com/problem/fizz-buzz/description?_from=ladder&&fromId=6)
给你一个整数n. 从 1 到 n 按照下面的规则打印每个数：

如果这个数被3整除，打印fizz.
如果这个数被5整除，打印buzz.
如果这个数能同时被3和5整除，打印fizz buzz.
如果这个数既不能被 3 整除也不能被 5 整除，打印数字本身。
"""


class Solution:
    def fizzBuzz(self, n: int):
        """
        @param n: An integer
        @return: A list of strings.
        """
        res = [x for x in range(1, n + 1)]
        for i, num in enumerate(res):
            if num % 15 == 0:
                res[i] = 'fizz buzz'
            elif num % 5 == 0:
                res[i] = 'buzz'
            elif num % 3 == 0:
                res[i] = 'fizz'
            else:
                res[i] = str(num)
        return res
