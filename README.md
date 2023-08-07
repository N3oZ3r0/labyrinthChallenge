# Minimal Moves in a Labyrinth

## Problem Overview

The challenge is to find the minimal number of moves required to carry a rod through a labyrinth. The rod is represented as a 1 × 3 rectangle, and it is initially positioned horizontally at the top-left corner of the labyrinth. The labyrinth itself is represented as a rectangular matrix, with some cells marked as blocked.

## Project Developer
        
- **Francisco Afán Rodríguez**     
[<img src="https://avatars1.githubusercontent.com/u/45666661?s=400&v=4" width="100px;"/><sub><b></b></sub>](https://github.com/N3oZ3r0)&nbsp;&nbsp;&nbsp;&nbsp;

### Objective

Move the rod to the bottom-right corner of the labyrinth using the fewest moves possible. If it's impossible to reach the destination, the function returns -1.

### Allowed Moves

1. Move the rod one cell down or up.
2. Move the rod one cell to the right or left.
3. Change the rod's orientation from vertical to horizontal or vice versa.

### Constraints

The rod can't collide with the blocked cells or the walls. It can only be rotated about its center, and only if the 3 × 3 area surrounding it is clear from the obstacles or walls.

## Function Signature

```python
def minimalMoves(labyrinth: List[List[str]]) -> int:
```

### Input

- `labyrinth`: A rectangular array of chars representing the labyrinth, where `labyrinth[i][j] = '.'` if the corresponding cell is empty and `labyrinth[i][j] = '#'` if the corresponding cell is blocked.

### Output

- An integer representing the number of moves required to carry the rod to the end of the labyrinth or -1 if it's impossible.

### Guaranteed Constraints

- `3 ≤ labyrinth.length ≤ 1000`
- `3 ≤ labyrinth[i].length ≤ 1000`

## Example

```python
labyrinth = [[".",".","."],
             [".",".","."],
             [".",".","."]]
print(minimalMoves(labyrinth)) # Output: 2
```

## Implementation Details

The solution is implemented using a breadth-first search algorithm. It explores all possible moves and orientations, maintaining a queue to iteratively examine each state. Constraints are applied to ensure that the moves and rotations are valid, following the rules described in the problem statement.

## Testing the Code

Example test cases are provided in the code to validate the implementation against various scenarios, including edge cases and different labyrinth configurations.