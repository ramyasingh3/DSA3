import heapq

class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        - small is a max heap containing smaller half of numbers
        - large is a min heap containing larger half of numbers
        """
        self.small = []  # max heap (invert numbers to simulate max heap)
        self.large = []  # min heap
        
    def addNum(self, num: int) -> None:
        """
        Adds a number into the data structure.
        
        Args:
            num: Integer to add
        """
        # Push to max heap by default
        heapq.heappush(self.small, -num)
        
        # Make sure every number in small is <= every number in large
        if self.small and self.large and -self.small[0] > self.large[0]:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
            
        # Balance heaps
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)
            
    def findMedian(self) -> float:
        """
        Returns the median of all numbers added so far.
        
        Returns:
            float: The median value
        """
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2

def test_median_finder():
    # Test cases
    finder = MedianFinder()
    
    test_cases = [
        (1, 1.0),
        (2, 1.5),
        (3, 2.0),
        (4, 2.5),
        (5, 3.0),
        (6, 3.5),
        (7, 4.0)
    ]
    
    print("Testing MedianFinder...")
    for num, expected in test_cases:
        finder.addNum(num)
        result = finder.findMedian()
        print(f"After adding {num}:")
        print(f"Expected median: {expected}")
        print(f"Actual median: {result}")
        print(f"Test {'passed' if abs(result - expected) < 0.0001 else 'failed'}")
        print("-" * 50)
        
    # Test empty case
    empty_finder = MedianFinder()
    print("Testing empty MedianFinder:")
    empty_finder.addNum(1)
    print(f"Added 1, median = {empty_finder.findMedian()}")
    print("Test passed" if abs(empty_finder.findMedian() - 1.0) < 0.0001 else "Test failed")

if __name__ == "__main__":
    test_median_finder() 