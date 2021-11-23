from collections import deque

def solve_puzzle(board, source, destination):
    """
    Given a 2-D matrix of cells that are empty or contain a barrier
    Returns the path of cells to reach the destination
    """
    # store the directional moves
    moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    # keep track of each layer in BFS
    move_count = 0
    current_layer = 1
    next_layer = 0
    # visited matrix stores 0 if not visited or previous cell
    visited = [[0 for x in range(len(board[0]))] for x in range(len(board))]
    # process the next moves in the unexplored queue
    unexplored = deque([source,])
    while unexplored:
        x, y = unexplored.popleft()
        # generate the path if the cell is the destination
        if (x, y) == destination:
            return generate_path(visited, source, destination)
        # explore neighboring cells
        for x_move, y_move in moves:
            new_x, new_y = x + x_move, y + y_move
            next_cell = (new_x, new_y)
            # only move to cells that are in bounds and not visited
            if is_valid_move(board, next_cell) and not visited[new_x][new_y]:
                unexplored.append(next_cell)
                visited[new_x][new_y] = (x, y)
                next_layer += 1
        current_layer -= 1
        # increment move count for each layer in BFS
        if current_layer == 0:
            move_count += 1
            current_layer = next_layer
            next_layer = 0
    # no path found
    return None

def is_valid_move(board, cell):
    """
    Helper function to determine valid moves
    """
    m, n = len(board), len(board[0])
    x, y = cell
    if 0 <= x < m and 0 <= y < n and board[x][y] != '#':
        return True
    return False

def generate_path(visited_board, source, dest):
    """
    Helper function to generate the path
    """
    moves = {(0, 1): 'R',
            (0, -1): 'L',
             (1, 0): 'D',
            (-1, 0): 'U'}
    path = [dest,]
    commands = []
    # traverse backwards through the path until source
    x, y = dest
    while source not in path:
        prev = visited_board[x][y]
        path.append(prev)
        commands.append(moves[(x - prev[0], y - prev[1])])
        x, y = prev
    # reverse back to correct order
    path.reverse()
    commands.reverse()
    return path, commands

