""" [替换空格](https://www.lintcode.com/problem/space-replacement/description?_from=ladder&&fromId=6)
设计一种方法，将一个字符串中的所有空格替换成 %20 。你可以假设该字符串有足够的空间来加入新的字符，且你得到的是“真实的”字符长度。
你的程序还需要返回被替换后的字符串的长度。
"""


class Solution:
    def replace_whitespace(self, s: list, length: int) -> None:
        if length == 0:
            return
        for i in range(length - 1, -1, -1):
            if s[i] == ' ':
                length += 2
                for j in range(length - 1, i - 1, -1):
                    s[j] = s[j - 2]
                s[i], s[i + 1], s[i + 2] = '%', '2', '0'
        return
