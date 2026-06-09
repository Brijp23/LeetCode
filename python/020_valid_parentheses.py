# 20. Valid Parentheses — Easy
# https://leetcode.com/problems/valid-parentheses/
#
# Determine if a string of brackets is valid (correctly opened and closed).
#
# Approach: stack — push opening brackets, pop and match on closing.
# Time: O(n)  Space: O(n)


def is_valid(s: str) -> bool:
    stack = []
    match = {')': '(', '}': '{', ']': '['}
    for ch in s:
        if ch in match:
            if not stack or stack[-1] != match[ch]:
                return False
            stack.pop()
        else:
            stack.append(ch)
    return len(stack) == 0


if __name__ == "__main__":
    assert is_valid("()")       == True
    assert is_valid("()[]{}")   == True
    assert is_valid("(]")       == False
    assert is_valid("([)]")     == False
    assert is_valid("{[]}")     == True
    print("All tests passed.")
