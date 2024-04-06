// https://leetcode.com/problems/contains-duplicate/

// Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

// Sol 1 - Hash Map, O (n) space time

public class Solution {
    public bool ContainsDuplicate(int[] nums) {
        Dictionary<int, int> seen = new Dictionary<int, int>();
        for (int i = 0; i < nums.Length; i ++) {
            if (seen.ContainsKey(nums[i])) {
                return true; 
            }
            seen[nums[i]] = 1;
        }
        return false;
    }
}

// Sol 2 - Hash set, O(n) space time 

public class Solution {
    public bool ContainsDuplicate(int[] nums) {
        HashSet<int> seen = new HashSet<int>();

        foreach (int num in nums) {
            if (seen.Contains(num)) {
                return true;
            }
            seen.Add(num);
        }
        return false;
    }
}

// Sol 3 - Array sort O(nlogn) time, O(1) space

public class Solution {
    public bool ContainsDuplicate(int[] nums) {
        Array.Sort(nums); 
        for (int i = 0; i < nums.Length - 1; i++) {
            if (nums[i] == nums[i + 1]) {
                return true;
            }
        }
        return false;
    }
}