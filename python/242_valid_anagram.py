# 242. Valid Anagram — Easy
# https://leetcode.com/problems/valid-anagram/
#
# Determine if two strings are anagrams of each other.
#
# Approach: character frequency count using a single dictionary.
# Time: O(n)  Space: O(1) — at most 26 keys

from collections import Counter


def is_anagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


if __name__ == "__main__":
    assert is_anagram("anagram", "nagaram") == True
    assert is_anagram("rat",     "car")     == False
    assert is_anagram("a",       "ab")      == False
    print("All tests passed.")
