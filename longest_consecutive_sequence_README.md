# Longest Consecutive Sequence

## Problem Statement
Given an unsorted array of integers `nums`, return the length of the longest consecutive sequence of numbers.

A consecutive sequence is a sequence of numbers where each number is one more than the previous number.

### Example 1:
```
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive sequence is [1,2,3,4]. Therefore its length is 4.
```

### Example 2:
```
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Explanation: The longest consecutive sequence is [0,1,2,3,4,5,6,7,8]. Therefore its length is 9.
```

### Example 3:
```
Input: nums = [1,1,1,1]
Output: 1
Explanation: The longest consecutive sequence is [1]. Therefore its length is 1.
```

## Constraints:
- 0 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9

## Solution Approach
The solution uses a HashSet to solve this problem efficiently:

1. Convert the input array to a set for O(1) lookups.

2. For each number in the set:
   - Check if it's the start of a sequence (i.e., num-1 is not in the set)
   - If it is, count the length of the sequence by checking consecutive numbers
   - Keep track of the maximum length found

3. Return the maximum length

## Time and Space Complexity
- Time Complexity: O(n), where n is the length of the input array
- Space Complexity: O(n) for the HashSet

## Implementation
The solution is implemented in Python using a set. The code includes test cases to verify the implementation. 