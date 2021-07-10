DEAD_CELL = 0
ALIVE_CELL = 1

def next_gen(cells):
    if not cells:
        return cells
    rows = len(cells)
    cols = len(cells[0])    
    new_cells = [([0]*cols) for _ in range(rows)]
    for i in range(rows):
        for k in range(cols):
            sum = sum_neighbours_cells(cells,i,k)
            cell = cells[i][k]
            if is_alive(cell, sum):
                new_cells[i][k] = ALIVE_CELL
            else:
                new_cells[i][k] = DEAD_CELL
    return new_cells

def is_alive(cell, sum):
    if (sum == 3) or (cell == ALIVE_CELL and sum == 2):
        return True
    return False

def sum_neighbours_cells(cells, cell_x, cell_y):
    NEIGHBORS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    return sum(get_cell(cells, cell_x + i,cell_y + k) for i,k in NEIGHBORS)
    

def get_cell(cells, i, k):    
    if is_in_boundaries(cells, i, k):
        return cells[i][k]
    return DEAD_CELL    
    
def is_in_boundaries(cells, i, k):
    return (0 <= i < len(cells)) and (0 <= k < len(cells[0]))