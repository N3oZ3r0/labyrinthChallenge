from collections import deque

# Check if the movement is possible
def isValidMove(labyrinth, x, y, horizontal):
    if horizontal:
        return all(labyrinth[x][ny] == '.' for ny in range(y - 1, y + 2)) if 0 <= x < len(labyrinth) and 1 <= y < len(labyrinth[0]) - 1 else False
    else:
        return all(labyrinth[nx][y] == '.' for nx in range(x - 1, x + 2)) if 1 <= x < len(labyrinth) - 1 and 0 <= y < len(labyrinth[0]) else False

# Check if rotation is possible
def canRotate(labyrinth, x, y):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not (0 <= x + i < len(labyrinth) and 0 <= y + j < len(labyrinth[0]) and labyrinth[x + i][y + j] == '.'):
                return False
    return True

# Main function
def minimalMoves(labyrinth):
    print("\nLabyrinth:")
    for r in labyrinth:
        print(*r)

    rows, cols = len(labyrinth), len(labyrinth[0])

    # Check the constraints
    if rows < 3 or rows > 1000 or cols < 3 or cols > 1000:
        raise ValueError("Labyrinth dimensions are outside the guaranteed constraints")

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] # right, left, down, up
    queue = deque([(0, 1, True, 0)]) # x, y, horizontal, moves
    visited = set([(0, 1, True)])

    # Loop condition until a result is reached
    while queue:
        x, y, horizontal, moves = queue.popleft()

        if (horizontal and x == rows - 1 and y == cols - 2) or (not horizontal and x == rows - 2 and y == cols - 1):
            return 'result: %i' % (moves)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if isValidMove(labyrinth, nx, ny, horizontal) and (nx, ny, horizontal) not in visited:
                visited.add((nx, ny, horizontal))
                queue.append((nx, ny, horizontal, moves + 1))

        if canRotate(labyrinth, x, y) and (x, y, not horizontal) not in visited:
            visited.add((x, y, not horizontal))
            queue.append((x, y, not horizontal, moves + 1))
    
    return 'result: %i' % (-1)

labyrinth = [[".",".",".",".",".",".",".",".","."],["#",".",".",".","#",".",".",".","."],[".",".",".",".","#",".",".",".","."],[".","#",".",".",".",".",".","#","."],[".","#",".",".",".",".",".","#","."]]
print(minimalMoves(labyrinth))

labyrinth = [[".",".",".",".",".",".",".",".","."],["#",".",".",".","#",".",".","#","."],[".",".",".",".","#",".",".",".","."],[".","#",".",".",".",".",".","#","."],[".","#",".",".",".",".",".","#","."]]
print(minimalMoves(labyrinth))

labyrinth = [[".",".","."],[".",".","."],[".",".","."]]
print(minimalMoves(labyrinth))

labyrinth = [[".",".",".",".",".",".",".",".",".","."],[".","#",".",".",".",".","#",".",".","."],[".","#",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".",".","."],[".","#",".",".",".",".",".",".",".","."],[".","#",".",".",".","#",".",".",".","."],[".",".",".",".",".",".","#",".",".","."],[".",".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".",".","."]]
print(minimalMoves(labyrinth))