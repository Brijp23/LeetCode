# 733. Flood Fill — Easy
# https://leetcode.com/problems/flood-fill/
#
# Perform a flood fill on an image starting from pixel (sr, sc).
#
# Approach: BFS from the starting pixel, replacing the old color.
# Time: O(m * n)  Space: O(m * n)

from typing import List
from collections import deque


def flood_fill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    old_color = image[sr][sc]
    if old_color == color:
        return image

    rows, cols = len(image), len(image[0])
    queue = deque([(sr, sc)])
    image[sr][sc] = color

    while queue:
        r, c = queue.popleft()
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == old_color:
                image[nr][nc] = color
                queue.append((nr, nc))

    return image


if __name__ == "__main__":
    img = [[1,1,1],[1,1,0],[1,0,1]]
    assert flood_fill(img, 1, 1, 2) == [[2,2,2],[2,2,0],[2,0,1]]
    print("All tests passed.")
