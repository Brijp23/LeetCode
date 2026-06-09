// 70. Climbing Stairs — Easy
// https://leetcode.com/problems/climbing-stairs/
//
// Count distinct ways to climb n stairs, taking 1 or 2 steps at a time.
//
// Approach: dynamic programming (Fibonacci pattern).
// Time: O(n)  Space: O(1)

public class ClimbingStairs {
    public int climbStairs(int n) {
        if (n <= 2) return n;
        int prev2 = 1, prev1 = 2;
        for (int i = 3; i <= n; i++) {
            int cur = prev1 + prev2;
            prev2   = prev1;
            prev1   = cur;
        }
        return prev1;
    }

    public static void main(String[] args) {
        ClimbingStairs sol = new ClimbingStairs();
        assert sol.climbStairs(2) == 2;
        assert sol.climbStairs(3) == 3;
        assert sol.climbStairs(5) == 8;
        System.out.println("All tests passed.");
    }
}
