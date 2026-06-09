# 206. Reverse Linked List — Easy
# https://leetcode.com/problems/reverse-linked-list/
#
# Reverse a singly linked list.
#
# Approach: iterative — three-pointer walk.
# Time: O(n)  Space: O(1)

from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val  = val
        self.next = next


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    prev, cur = None, head
    while cur:
        nxt       = cur.next
        cur.next  = prev
        prev, cur = cur, nxt
    return prev


def to_list(node):
    r = []
    while node:
        r.append(node.val)
        node = node.next
    return r

def from_list(vals):
    dummy = ListNode()
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


if __name__ == "__main__":
    assert to_list(reverse_list(from_list([1,2,3,4,5]))) == [5,4,3,2,1]
    assert to_list(reverse_list(from_list([1,2])))       == [2,1]
    assert to_list(reverse_list(from_list([])))          == []
    print("All tests passed.")
