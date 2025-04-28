def longest_increasing_path(matrix: list[list[int]]) -> int:
    """
    Find the length of the longest increasing path in a matrix.
    
    Args:
        matrix (list[list[int]]): 2D matrix of integers
        
    Returns:
        int: Length of the longest increasing path
    """
    if not matrix or not matrix[0]:
        return 0
        
    m, n = len(matrix), len(matrix[0])
    dp = [[0] * n for _ in range(m)]
    
    def dfs(i: int, j: int) -> int:
        if dp[i][j] != 0:
            return dp[i][j]
            
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        max_path = 1
        
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                max_path = max(max_path, dfs(ni, nj) + 1)
                
        dp[i][j] = max_path
        return max_path
    
    max_length = 0
    for i in range(m):
        for j in range(n):
            max_length = max(max_length, dfs(i, j))
    
    return max_length

def main():
    # Test cases
    test_cases = [
        [
            [9, 9, 4],
            [6, 6, 8],
            [2, 1, 1]
        ],  # Expected: 4 (path: 1 -> 2 -> 6 -> 9)
        [
            [3, 4, 5],
            [3, 2, 6],
            [2, 2, 1]
        ],  # Expected: 4 (path: 1 -> 2 -> 3 -> 4)
        [
            [1]
        ],  # Expected: 1
        [],  # Expected: 0
        [
            [1, 2],
            [3, 4]
        ],  # Expected: 4 (path: 1 -> 2 -> 4)
    ]
    
    for matrix in test_cases:
        result = longest_increasing_path(matrix)
        print(f"Input: matrix = {matrix}")
        print(f"Output: {result}\n")

if __name__ == "__main__":
    main() 