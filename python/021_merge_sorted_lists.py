# 21. Merge Two Sorted Lists — Easy
# https://leetcode.com/problems/merge-two-sorted-lists/
#
# Merge two sorted linked lists and return the merged sorted list.
#
# Approach: iterative with a dummy head node — compare heads, advance the smaller.
# Time: O(m + n)  Space: O(1)

from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val  = val
        self.next = next


def merge_two_lists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    cur   = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            cur.next, l1 = l1, l1.next
        else:
            cur.next, l2 = l2, l2.next
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next


def to_list(node: Optional[ListNode]) -> list:
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


def from_list(vals: list) -> Optional[ListNode]:
    dummy = ListNode()
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


if __name__ == "__main__":
    assert to_list(merge_two_lists(from_list([1,2,4]), from_list([1,3,4]))) == [1,1,2,3,4,4]
    assert to_list(merge_two_lists(from_list([]),      from_list([])))      == []
    assert to_list(merge_two_lists(from_list([]),      from_list([0])))     == [0]
    print("All tests passed.")
