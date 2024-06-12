from collections import deque
import heapq
from coordinates import Directions, Coordinates, Action
from models.trash_truck import check_collision, WIDTH, HEIGHT, SQUARE_SIZE
from gui.grid_one import get_road_type, check_row, check_col

GRID_SIZE = 32

def is_valid(row, col):
    return (row >= 0) and (row < GRID_SIZE*25) and (col >= 0) and (col < GRID_SIZE*25)

def is_destination(row, col, dest: Coordinates):
    return row == dest.x and col == dest.y

# heuristics - using Manhattan Distance
def heuristics(row, col, dir: Directions, dest: Coordinates):
    manhattan_distance = ((abs(row - dest.x) + abs(col - dest.y))/25)
    return manhattan_distance

def trace_path(cell_details, dest: Coordinates):
    print("The Path is ")
    path = []
    row = dest.x
    col = dest.y
    dir = Directions.DOWN
    action = None
    row_grid = row // 25
    col_grid = col // 25

    for i in range(4):
        if cell_details[row_grid][col_grid][i].parent_x >= 0:
            dir = Directions(i)
            action = cell_details[row_grid][col_grid][i].action

    # Trace the path from destination to source using parent cells
    while not (cell_details[row_grid][col_grid][dir.value].parent_x == row and cell_details[row_grid][col_grid][dir.value].parent_y == col and cell_details[row_grid][col_grid][dir.value].parent_dir == dir):
        action = cell_details[row_grid][col_grid][dir.value].action
        path.append(action)
        temp_row = cell_details[row_grid][col_grid][dir.value].parent_x
        temp_col = cell_details[row_grid][col_grid][dir.value].parent_y
        temp_dir = cell_details[row_grid][col_grid][dir.value].parent_dir
        row = temp_row
        col = temp_col
        dir = temp_dir

        row_grid = row // 25
        col_grid = col // 25

    # Reverse the path to get the path from source to destination
    path.reverse()
    print(path)
    return path

def a_star_search(src: Coordinates, dest: Coordinates):
    if not is_valid(src.x, src.y) or not is_valid(dest.x, dest.y):
        print("Source or destination is invalid")
        return
 
    if is_destination(src.x, src.y, dest):
        print("We are already at the destination")
        return
 
    # Closed list - fields that were already visited, including the direction
    closed_list = [[[False for _ in range(4)] for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    # Details of each cell
    cell_details = [[[Coordinates() for _ in range(4)] for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

    # Start cell details
    i = src.x
    j = src.y
    dir = src.direction
    i_grid = int(i/25)
    j_grid = int(j/25)
    cell_details[i_grid][j_grid][dir.value].f = 0
    cell_details[i_grid][j_grid][dir.value].g = 0
    cell_details[i_grid][j_grid][dir.value].h = 0
    cell_details[i_grid][j_grid][dir.value].x = i
    cell_details[i_grid][j_grid][dir.value].y = j
    cell_details[i_grid][j_grid][dir.value].dir = dir
    cell_details[i_grid][j_grid][dir.value].parent_x = i
    cell_details[i_grid][j_grid][dir.value].parent_y = j
    cell_details[i_grid][j_grid][dir.value].parent_dir = dir
 
    # Open list - cells to be visited
    open_list = []
    heapq.heappush(open_list, (0.0, i, j, dir))
 
    found_dest = False
 
    # Main loop of A* search algorithm
    while len(open_list) > 0:
        # Pop the cell with the smallest f value from the open list
        p = heapq.heappop(open_list)
        # Mark the cell as visited
        i = p[1]
        j = p[2]
        i_grid = int(i/25)
        j_grid = int(j/25)
        dir = Directions(p[3])
        closed_list[i_grid][j_grid][dir.value] = True
        parent = cell_details[i_grid][j_grid][dir.value]
        # For each direction, check the successors
        succs = get_succ(i, j, dir)
        for succ in succs:
            new_i = succ.x
            new_j = succ.y
            new_dir = succ.direction
            action = succ.action
            new_i_grid = int(new_i/25)
            new_j_grid = int(new_j/25)
            # If the successor is valid and not visited
            if is_valid(new_i, new_j) and closed_list[new_i_grid][new_j_grid][new_dir.value] == False :
                if is_destination(new_i, new_j, dest):
                    cell_details[new_i_grid][new_j_grid][new_dir.value].x = new_i
                    cell_details[new_i_grid][new_j_grid][new_dir.value].y = new_j
                    cell_details[new_i_grid][new_j_grid][new_dir.value].dir = new_dir
                    cell_details[new_i_grid][new_j_grid][new_dir.value].parent_x = i
                    cell_details[new_i_grid][new_j_grid][new_dir.value].parent_y = j
                    cell_details[new_i_grid][new_j_grid][new_dir.value].parent_dir = dir
                    cell_details[new_i_grid][new_j_grid][new_dir.value].action = action
                    result = trace_path(cell_details, dest)
                    found_dest = True
                    return result
                else:
                    # Calculate the new f, g, and h values
                    cell_details[new_i_grid][new_j_grid][new_dir.value].x = new_i
                    cell_details[new_i_grid][new_j_grid][new_dir.value].y = new_j
                    cell_details[new_i_grid][new_j_grid][new_dir.value].dir = new_dir
                    g_old = parent.g
                    g_new = 1.0 + get_road_type(i, j)
                    if (action != Action.forward):
                        g_new /= 2
                    g_new += g_old
                    h_new = heuristics(new_i, new_j, new_dir, dest)
                    f_new = g_new + h_new
                    '''
                    print(new_i_grid, new_j_grid, new_dir)
                    print("parent:", i_grid, j_grid, dir, "g:", g_old)
                    print("g value:", g_new)
                    print("f value:", f_new)
                    '''
                    # If the cell is not in the open list or the new f value is smaller
                    if cell_details[new_i_grid][new_j_grid][new_dir.value].f == float('inf') or cell_details[new_i_grid][new_j_grid][new_dir.value].f > f_new:
                        # Add the cell to the open list
                        heapq.heappush(open_list, (f_new, new_i, new_j, new_dir.value))
                        cell_details[new_i_grid][new_j_grid][new_dir.value].f = f_new
                        cell_details[new_i_grid][new_j_grid][new_dir.value].g = g_new
                        cell_details[new_i_grid][new_j_grid][new_dir.value].h = h_new
                        cell_details[new_i_grid][new_j_grid][new_dir.value].parent_x = i
                        cell_details[new_i_grid][new_j_grid][new_dir.value].parent_y = j
                        cell_details[new_i_grid][new_j_grid][new_dir.value].parent_dir = dir
                        cell_details[new_i_grid][new_j_grid][new_dir.value].action = action

    # If the destination is not found after visiting all cells
    if not found_dest:
        print("Failed to find the destination cell")
        return None

def get_succ(x, y, dir: Directions):
    result = []
    # Move forward
    match dir:
        case Directions.UP:
            result.append(Coordinates(x, y - 25, dir, Action.forward))
        case Directions.LEFT:
            result.append(Coordinates(x - 25, y, dir, Action.forward))
        case Directions.DOWN:
            result.append(Coordinates(x, y + 25, dir, Action.forward))
        case Directions.RIGHT:
            result.append(Coordinates(x + 25, y, dir, Action.forward))

    # Turn left
    left_direction = Directions((dir.value - 1) % 4)
    result.append(Coordinates(x, y, left_direction, Action.left))

    # Turn right
    right_direction = Directions((dir.value + 1) % 4)
    result.append(Coordinates(x, y, right_direction, Action.right))
    return result

def move_direction(start_coordinates : Coordinates, acton: Action):
    x = start_coordinates.x
    y = start_coordinates.y
    dir = start_coordinates.direction
    if (acton == Action.forward):
        match (dir):
            case Directions.UP:
                return Coordinates(x, y - 25, dir, Action.forward)
            case Directions.LEFT:
                return Coordinates(x - 25, y, dir, Action.forward)
            case Directions.DOWN:
                return Coordinates(x, y + 25, dir, Action.forward)
            case Directions.RIGHT:
                return Coordinates(x + 25, y, dir, Action.forward)
    elif acton == Action.left:
        return Coordinates(x, y, Directions((dir.value - 1) % 4))
    else:
        return Coordinates(x, y, Directions((dir.value + 1) % 4))

def calc_rotation(direction):
    if direction == Directions.UP:
        return 90
    elif direction == Directions.DOWN:
        return 270
    elif direction == Directions.LEFT:
        return 180
    else:
        return 0

def check_flip(direction):
    return direction == Directions.LEFT.value
