# 53. Maximum Subarray — Medium
# https://leetcode.com/problems/maximum-subarray/
#
# Find the contiguous subarray with the largest sum.
#
# Approach: Kadane's algorithm — track running sum, reset when it goes negative.
# Time: O(n)  Space: O(1)

from typing import List


def max_subarray(nums: List[int]) -> int:
    max_sum = cur_sum = nums[0]
    for num in nums[1:]:
        cur_sum = max(num, cur_sum + num)
        max_sum = max(max_sum, cur_sum)
    return max_sum


if __name__ == "__main__":
    assert max_subarray([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert max_subarray([1])                      == 1
    assert max_subarray([5,4,-1,7,8])             == 23
    print("All tests passed.")
