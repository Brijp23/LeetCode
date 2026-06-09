# 283. Move Zeroes — Easy
# https://leetcode.com/problems/move-zeroes/
#
# Move all zeroes to the end while maintaining relative order of non-zero elements.
# Must be done in-place.
#
# Approach: two-pointer — write pointer tracks next non-zero position.
# Time: O(n)  Space: O(1)

from typing import List


def move_zeroes(nums: List[int]) -> None:
    write = 0
    for num in nums:
        if num != 0:
            nums[write] = num
            write += 1
    for i in range(write, len(nums)):
        nums[i] = 0


if __name__ == "__main__":
    a = [0,1,0,3,12]
    move_zeroes(a)
    assert a == [1,3,12,0,0]

    b = [0]
    move_zeroes(b)
    assert b == [0]

    print("All tests passed.")
