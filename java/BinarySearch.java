// 704. Binary Search — Easy
// https://leetcode.com/problems/binary-search/
//
// Search for a target in a sorted array. Return index or -1.
//
// Approach: classic iterative binary search.
// Time: O(log n)  Space: O(1)

public class BinarySearch {
    public int search(int[] nums, int target) {
        int lo = 0, hi = nums.length - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if      (nums[mid] == target) return mid;
            else if (nums[mid] <  target) lo = mid + 1;
            else                          hi = mid - 1;
        }
        return -1;
    }

    public static void main(String[] args) {
        BinarySearch sol = new BinarySearch();
        assert sol.search(new int[]{-1,0,3,5,9,12}, 9)  ==  4;
        assert sol.search(new int[]{-1,0,3,5,9,12}, 2)  == -1;
        System.out.println("All tests passed.");
    }
}
