# 704. Binary Search — Easy
# https://leetcode.com/problems/binary-search/
#
# Search for a target in a sorted array. Return its index or -1 if not found.
#
# Approach: classic binary search.
# Time: O(log n)  Space: O(1)

from typing import List


def search(nums: List[int], target: int) -> int:
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


if __name__ == "__main__":
    assert search([-1,0,3,5,9,12], 9)  ==  4
    assert search([-1,0,3,5,9,12], 2)  == -1
    assert search([5],             5)  ==  0
    print("All tests passed.")
