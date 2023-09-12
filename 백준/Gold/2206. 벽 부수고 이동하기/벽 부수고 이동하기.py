from collections import deque

def shortest_path(N, M, matrix):
    # Initialize distances array with -1
    distances = [[[-1 for _ in range(M)] for _ in range(N)] for _ in range(2)]
    # Initialize queue for BFS
    queue = deque()
    # Add starting point to queue
    queue.append((0, 0, 0))
    # Set distance of starting point to 1
    distances[0][0][0] = 1
    # Define directions for movement
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while queue:
        x, y, z = queue.popleft()
        if x == N-1 and y == M-1:
            return distances[z][x][y]
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if nx >= 0 and nx < N and ny >= 0 and ny < M:
                if matrix[nx][ny] == '0' and distances[z][nx][ny] == -1:
                    distances[z][nx][ny] = distances[z][x][y] + 1
                    queue.append((nx, ny, z))
                elif z == 0 and matrix[nx][ny] == '1' and distances[1][nx][ny] == -1:
                    distances[1][nx][ny] = distances[z][x][y] + 1
                    queue.append((nx, ny, 1))
    return -1

# Example test case
N, M = map(int, input().split())
matrix = [list(input()) for _ in range(N)]
print(shortest_path(N, M, matrix)) # Output: 15