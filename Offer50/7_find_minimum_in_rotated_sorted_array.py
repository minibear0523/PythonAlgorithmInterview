""" [寻找旋转排序数组中的最小值](https://www.lintcode.com/problem/find-minimum-in-rotated-sorted-array/description?_from=ladder&&fromId=6)
假设一个排好序的数组在其某一未知点发生了旋转（比如0 1 2 4 5 6 7 可能变成4 5 6 7 0 1 2）。你需要找到其中最小的元素。
"""


class Solution:
    def find_min(self, nums: list):
        if not nums:
            return None
        elif nums[0] < nums[-1]:
            return nums[0]

        length = len(nums)
        left, right = 0, length - 1
        while left <= right:
            mid = left + ((right - left) >> 1)
            if mid == 0 or nums[mid] < nums[mid-1]:
                return nums[mid]
            elif nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1
        return None
