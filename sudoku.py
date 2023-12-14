from typing import List, Tuple

count_numbers_added: int
count_numbers_backtracked: int

GRID = [
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0],
]

def solve_sudoku_puzzle():
    global count_numbers_added
    global count_numbers_backtracked
    count_numbers_added = count_numbers_backtracked = 0

    grid = [row[:] for row in GRID]

    grid_solved = _solve_puzzle(grid)

    if grid_solved:
        for row in grid:
            print(row)
        print(f'Numbers put into the Sudoku puzzle: {count_numbers_added}')
        print(f'Numbers that had to be backtracked due to a dead-end: {count_numbers_backtracked}')

    else:
        raise Exception('No solution found!')

def _check_valid_number(y: int, x: int, n: int, grid: List[List[int]]) -> bool:
  
    row_column_size = range(len(grid))
    for i in row_column_size:
        if grid[y][i] == n or grid[i][x] == n:
          
            return False
          
    block_size = 3
    x_block = (x // block_size) * block_size
    y_block = (y // block_size) * block_size
    for i in range(block_size):
        for j in range(block_size):
          
            if grid[y_block + i][x_block + j] == n:
                return False
              
    return True

def _solve_puzzle(grid: List[List[int]]) -> Tuple[int, int]:
    global count_numbers_added
    global count_numbers_backtracked

    row_column_size = len(grid)
    for y in range(row_column_size):
        for x in range(row_column_size):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if _check_valid_number(y, x, n, grid):
                        grid[y][x] = n
                      
                        count_numbers_added += 1
                      
                        if _solve_puzzle(grid):
                          
                            return count_numbers_added, count_numbers_backtracked
                        grid[y][x] = 0
                      
                        count_numbers_backtracked += 1
                return count_numbers_added, count_numbers_backtracked
    return count_numbers_added, count_numbers_backtracked

def main():
    solve_sudoku_puzzle()

if __name__ == '__main__':
    main()
