// 141. Linked List Cycle — Easy
// https://leetcode.com/problems/linked-list-cycle/
//
// Detect if a linked list has a cycle.
//
// Approach: Floyd's two-pointer (slow/fast). If they meet, there's a cycle.
// Time: O(n)  Space: O(1)

public class LinkedListCycle {
    static class ListNode {
        int val;
        ListNode next;
        ListNode(int val) { this.val = val; }
    }

    public boolean hasCycle(ListNode head) {
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) return true;
        }
        return false;
    }

    public static void main(String[] args) {
        LinkedListCycle sol = new LinkedListCycle();

        // cycle: 3 -> 2 -> 0 -> -4 -> (back to 2)
        ListNode n1 = new ListNode(3);
        ListNode n2 = new ListNode(2);
        ListNode n3 = new ListNode(0);
        ListNode n4 = new ListNode(-4);
        n1.next = n2; n2.next = n3; n3.next = n4; n4.next = n2;
        assert sol.hasCycle(n1) == true;

        // no cycle
        ListNode m1 = new ListNode(1);
        ListNode m2 = new ListNode(2);
        m1.next = m2;
        assert sol.hasCycle(m1) == false;

        System.out.println("All tests passed.");
    }
}
