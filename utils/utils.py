from collections import deque
import heapq
from coordinates import Directions, Coordinates
from models.trash_truck import check_collision, WIDTH, HEIGHT, SQUARE_SIZE

GRID_SIZE = 32

# TODO: fix trace_path

def is_valid(row, col):
    return (row >= 0) and (row < GRID_SIZE*25) and (col >= 0) and (col < GRID_SIZE*25)

def is_destination(row, col, dest: Coordinates):
    return row == dest.x and col == dest.y

## heuristics - using Manhattan Distance, including rotations (cost 0.5 each, not accurate) 
def heuristics(row, col, dir: Directions, dest: Coordinates):
    manhattan_distance = (abs(row - dest.x) + abs(col - dest.y))/25
    rotation = 0
    if col < dest.y:
        rotation += 2
    if row < dest.x:
        rotation += 3
    elif row > dest.x:
        rotation += 1
    rotation = abs(rotation - dir.value)
    rotation /= 2
    return manhattan_distance + rotation

def trace_path(cell_details, dest: Coordinates):
    print("The Path is ")
    path = []
    row = dest.x
    col = dest.y
    dir = Directions.DOWN
    row_grid = row // 25
    col_grid = col // 25

    for i in range(4):
        if cell_details[row_grid][col_grid][i].parent_x >= 0:
            dir = Directions(i)

    # Trace the path from destination to source using parent cells
    while not (cell_details[row_grid][col_grid][dir.value].parent_x == row and cell_details[row_grid][col_grid][dir.value].parent_y == col and cell_details[row_grid][col_grid][dir.value].parent_dir == dir):
        path.append((row, col, dir))
        temp_row = cell_details[row_grid][col_grid][dir.value].parent_x
        temp_col = cell_details[row_grid][col_grid][dir.value].parent_y
        temp_dir = cell_details[row_grid][col_grid][dir.value].parent_dir

        row = temp_row
        col = temp_col
        dir = temp_dir

        row_grid = row // 25
        col_grid = col // 25

    # Add the source cell to the path
    path.append((row, col, dir))

    # Reverse the path to get the path from source to destination
    path.reverse()

    # Print the path
    for i in path:
        print("->", i, end=" ")
    print()


def a_star_search(src: Coordinates, dest: Coordinates):
    # Check if the source and destination are valid
    if not is_valid(src.x, src.y) or not is_valid(dest.x, dest.y):
        print("Source or destination is invalid")
        return
 
    # Check if we are already at the destination
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
    print(i, j, dir)
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
 
    # Flag for whether destination is found
    found_dest = False
 
    # Main loop of A* search algorithm
    while len(open_list) > 0:
        # Pop the cell with the smallest f value from the open list
        p = heapq.heappop(open_list)
        # Mark the cell as visited
        i = p[1]
        j = p[2]
        dir = Directions(p[3])
        closed_list[i_grid][j_grid][dir.value] = True
        # For each direction, check the successors
        succs = get_succ(i, j, dir)
        for succ in succs:
            new_i = succ.x
            new_j = succ.y
            new_dir = succ.direction
            new_i_grid = int(new_i/25)
            new_j_grid = int(new_j/25)
            # If the successor is valid and not visited
            if is_valid(new_i, new_j) and closed_list[new_i_grid][new_j_grid][new_dir.value] == False :
                # If the successor is the destination
                if is_destination(new_i, new_j, dest):
                    # Set the parent of the destination cell
                    cell_details[new_i_grid][new_j_grid][new_dir.value].parent_x = i
                    cell_details[new_i_grid][new_j_grid][new_dir.value].parent_y = j
                    cell_details[new_i_grid][new_j_grid][new_dir.value].parent_dir = dir
                    # Trace and print the path from source to destination
                    trace_path(cell_details, dest)
                    found_dest = True
                    return
                else:
                    # Calculate the new f, g, and h values
                    g_new = cell_details[i_grid][j_grid][dir.value].g + 1.0
                    h_new = heuristics(new_i, new_j, new_dir, dest)
                    f_new = g_new + h_new
                    # If the cell is not in the open list or the new f value is smaller
                    if cell_details[new_i_grid][new_j_grid][new_dir.value].f == float('inf') or cell_details[new_i_grid][new_j_grid][new_dir.value].f > f_new:
                        # Add the cell to the open list
                        heapq.heappush(open_list, (f_new, new_i, new_j, new_dir.value))
                        # Update the cell details
                        cell_details[new_i_grid][new_j_grid][new_dir.value].f = f_new
                        cell_details[new_i_grid][new_j_grid][new_dir.value].g = g_new
                        cell_details[new_i_grid][new_j_grid][new_dir.value].h = h_new
                        cell_details[new_i_grid][new_j_grid][new_dir.value].parent_x = i
                        cell_details[new_i_grid][new_j_grid][new_dir.value].parent_y = j
                        cell_details[new_i_grid][new_j_grid][new_dir.value].parent_dir = dir

    # If the destination is not found after visiting all cells
    if not found_dest:
        print("Failed to find the destination cell")

def get_succ(x, y, dir: Directions):
    
    result = []
    # Move forward
    match dir:
        case Directions.UP:
            result.append(Coordinates(x, y - 25, dir))
        case Directions.LEFT:
            result.append(Coordinates(x - 25, y, dir))
        case Directions.DOWN:
            result.append(Coordinates(x, y + 25, dir))
        case Directions.RIGHT:
            result.append(Coordinates(x + 25, y, dir))

    # Turn left
    left_direction = Directions((dir.value - 1) % 4)
    result.append(Coordinates(x, y, left_direction))

    # Turn right
    right_direction = Directions((dir.value + 1) % 4)
    result.append(Coordinates(x, y, right_direction))
    return result

def move_direction(start_coordinates, end_coordinates):
    if start_coordinates.x > end_coordinates.x and start_coordinates.y == end_coordinates.y:
        return Directions.LEFT.value
    if start_coordinates.x < end_coordinates.x and start_coordinates.y == end_coordinates.y:
        return Directions.RIGHT.value
    if start_coordinates.x == end_coordinates.x and start_coordinates.y > end_coordinates.y:
        return Directions.UP.value
    if start_coordinates.x == end_coordinates.x and start_coordinates.y < end_coordinates.y:
        return Directions.DOWN.value
'''
def find_shortest_path(coordinates: Coordinates, houses, target):
    start = (coordinates.x, coordinates.y)
    visited = set()
    queue = deque([[start]])
    while queue:
        path = queue.popleft()
        current = path[-1]
        if current == target:
            return path[1:]
        if current in visited:
            continue
        visited.add(current)
        for direction in [Directions.UP.value, Directions.DOWN.value, Directions.LEFT.value,
                          Directions.RIGHT.value]:
            neighbour = get_neighbour(current, direction)
            if neighbour[0] < 0 or neighbour[0] > WIDTH or neighbour[1] < 0 or neighbour[1] > HEIGHT:
                continue
            if neighbour not in roads:
                continue
            if (neighbour not in visited and
                    not check_collision(truck_coordinates=Coordinates(neighbour[0], neighbour[1]), houses=houses)):
                queue.append(path + [neighbour])
    return []

def get_neighbour(position, direction):
    if direction == Directions.UP.value:
        return position[0], position[1] - SQUARE_SIZE
    elif direction == Directions.DOWN.value:
        return position[0], position[1] + SQUARE_SIZE
    elif direction == Directions.LEFT.value:
        return position[0] - SQUARE_SIZE, position[1]
    elif direction == Directions.RIGHT.value:
        return position[0] + SQUARE_SIZE, position[1]
'''
def calc_rotation(direction):
    if direction == Directions.UP.value:
        return 90
    elif direction == Directions.DOWN.value:
        return 270
    elif direction == Directions.LEFT.value:
        return 180
    else:
        return 0

def check_flip(direction):
    return direction == Directions.LEFT.value
