# Find Median from Data Stream

## Problem Description
Design a data structure that supports adding integers and finding the median of all added numbers. The median is the middle value in an ordered integer list. If the size of the list is even, the median is the average of the two middle values.

### Examples
```
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.findMedian(); // return 1.0
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5
medianFinder.addNum(3);    // arr = [1, 2, 3]
medianFinder.findMedian(); // return 2.0
```

## Approach
The solution uses two heaps:
1. A max heap for the lower half of numbers
2. A min heap for the upper half of numbers

Key points:
- The max heap contains all numbers less than the median
- The min heap contains all numbers greater than the median
- The sizes of the heaps differ by at most 1
- If the total number of elements is odd, the extra element goes in the max heap

### Operations
1. Adding a number:
   - Compare with current median
   - Add to appropriate heap
   - Balance heaps if necessary
   
2. Finding median:
   - If heaps have equal size: average of tops
   - Otherwise: top of max heap

## Time Complexity
- addNum: O(log n)
- findMedian: O(1)
- where n is the number of elements in the data structure

## Space Complexity
- O(n) to store n numbers in the heaps 