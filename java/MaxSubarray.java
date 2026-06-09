// 53. Maximum Subarray — Medium
// https://leetcode.com/problems/maximum-subarray/
//
// Find the contiguous subarray with the largest sum.
//
// Approach: Kadane's algorithm.
// Time: O(n)  Space: O(1)

public class MaxSubarray {
    public int maxSubArray(int[] nums) {
        int maxSum = nums[0], curSum = nums[0];
        for (int i = 1; i < nums.length; i++) {
            curSum = Math.max(nums[i], curSum + nums[i]);
            maxSum = Math.max(maxSum, curSum);
        }
        return maxSum;
    }

    public static void main(String[] args) {
        MaxSubarray sol = new MaxSubarray();
        assert sol.maxSubArray(new int[]{-2,1,-3,4,-1,2,1,-5,4}) == 6;
        assert sol.maxSubArray(new int[]{1})                      == 1;
        assert sol.maxSubArray(new int[]{5,4,-1,7,8})             == 23;
        System.out.println("All tests passed.");
    }
}
