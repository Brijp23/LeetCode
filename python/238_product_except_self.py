# 238. Product of Array Except Self — Medium
# https://leetcode.com/problems/product-of-array-except-self/
#
# Return an array where each element is the product of all other elements.
# Must run in O(n) without using division.
#
# Approach: two passes — left prefix products, then right suffix products.
# Time: O(n)  Space: O(1) (output array not counted)

from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    n      = len(nums)
    result = [1] * n

    # left pass: result[i] = product of nums[0..i-1]
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix   *= nums[i]

    # right pass: multiply by product of nums[i+1..n-1]
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix    *= nums[i]

    return result


if __name__ == "__main__":
    assert product_except_self([1,2,3,4]) == [24,12,8,6]
    assert product_except_self([-1,1,0,-3,3]) == [0,0,9,0,0]
    print("All tests passed.")
