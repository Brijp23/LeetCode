// 1. Two Sum — Easy
// https://leetcode.com/problems/two-sum/
//
// Given an array and a target, return indices of the two numbers that sum to target.
//
// Approach: hash map — complement lookup in a single pass.
// Time: O(n)  Space: O(n)

import java.util.HashMap;

public class TwoSum {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> seen = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (seen.containsKey(complement)) {
                return new int[]{seen.get(complement), i};
            }
            seen.put(nums[i], i);
        }
        return new int[]{};
    }

    public static void main(String[] args) {
        TwoSum sol = new TwoSum();
        int[] r1 = sol.twoSum(new int[]{2,7,11,15}, 9);
        assert r1[0] == 0 && r1[1] == 1;
        int[] r2 = sol.twoSum(new int[]{3,2,4}, 6);
        assert r2[0] == 1 && r2[1] == 2;
        System.out.println("All tests passed.");
    }
}
