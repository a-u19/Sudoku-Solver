#Solve subsection
#day 1
def keyboard_input():
    solver_input = ""
    temp_input = ""
    for counter in range(9):
        valid_input = False
        while valid_input == False:
            temp_input = input("Enter the numbers in row {}.\n".format(counter + 1))
            if len(temp_input) != 9:
                print("Please enter only 9 digits")
            elif temp_input.isdigit() == False:
                print("Please only enter numbers")
            else:
                valid_input = True

#The user is prompted to make an input line by line, where each line is validated by checking if it only contains 9 characters and only has digits.
        solver_input = solver_input + temp_input

    curr_character = 0
    sudoku_grid = [[0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                 ]
                 
    for row in range(9):
        for column in range(9):
            sudoku_grid[row][column] = int(solver_input[curr_character])
            curr_character += 1
    print("\nThe inputted sudoku is:\n",)
    print('\n'.join('|'.join(str(x) for x in row) for row in sudoku_grid))

    return sudoku_grid

#day 2
def string_to_grid(string_input):
    sudoku_grid = [[0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                 ]
    counter = 0
    for column in range(9):
        for row in range(9):
            sudoku_grid[row][column] = int(string_input[counter])
            counter += 1
    return (sudoku_grid)

def grid_to_string(sudoku_grid):
    sudoku_str = ""
    for row in range(9):
        for column in range(9):
            sudoku_str += str(sudoku_grid[row][column])
    # return (sudoku_str.replace(0,""))
    return sudoku_str

#The function string_to_grid forms a grid from a string input and grid_to_string achieves the opposite. This becomes useful when converting between the two formats.

def row_check(sudoku_grid,value,row):
    for col in range(9):
        if (sudoku_grid[row][col]) == (value):
            return False
    return True
    
def col_check(sudoku_grid,value,col):
    for row in range(9):
        if (sudoku_grid[row][col]) == (value):
            return False
    return True

def subgrid_check(sudoku_grid,value,row,col):
    col = (col//3)*3 + 1
    row = (row//3)*3 + 1
    
    for x in [-1,0,1]:
        for y in [-1,0,1]:
            if (sudoku_grid[row+x][col+y]) == (value):
                return False
    return True
#####################################################################################################################################################################
#Generate subsection        
#day 4
#num_clues
def num_clues():
    valid = False
    while valid == False:
        user_input = input("Enter the number of clues that you want. This must be between 17 and 81.\n")
        if user_input.isdigit() == False:
            valid = False
        elif int(user_input)>81:
            valid = False
        elif int(user_input)<17:
            valid = False
        else:
            valid = True
        
        
    return int(user_input)   

#generate_clues
import random
def generate_clues():
    sudoku_grid = [[0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                 ]
    
    clue = 0
    num_of_clues = num_clues()
    while clue != num_of_clues:
        col = random.randint(0,8)
        row = random.randint(0,8)
        value = random.randint(1,9)
        value = str(value)
        if row_check(sudoku_grid,value,row) == True and col_check(sudoku_grid,value,col) == True and subgrid_check(sudoku_grid,value,row,col) == True:
            if sudoku_grid[row][col] == 0:
                sudoku_grid[row][col] = value
                clue += 1
        # else:
        #     print(("({} doesnt fit here").format(value))
            
    # print('\n'.join('|'.join(str(x) for x in row) for row in sudoku_grid))
    return sudoku_grid

#day 5    
#output final sudoku
def output(sudoku_grid):
    print("\nThe sudoku has been solved.\n")
    # print("The string output is: \n{}\n\nThe grid output is: \n{}".format(grid_to_string(sudoku_grid),('\n'.join('|'.join(str(x) for x in row) for row in sudoku_grid))))

#day 6
def find_unfilled(sudoku_grid):
    for row in range(0,9):
        for col in range(0,9):
            if sudoku_grid[row][col] == 0:
                return (row,col)
    return (-1,-1)

def solve_sudoku(sudoku_grid):
    x,y = find_unfilled(sudoku_grid)
    if x == -1 and y == -1:
        return True

    for num in range(1,10):
        if col_check(sudoku_grid,num,y) == True and row_check(sudoku_grid,num,x) == True and subgrid_check(sudoku_grid,num,x,y) == True:
            
            sudoku_grid[x][y] = num

            if solve_sudoku(sudoku_grid) == True:
                return True

            sudoku_grid[x][y] = 0

    return False

def solve_main(data):
    # data = generate_clues()
    # data = [[0,0,0,2,6,0,7,0,1],
    #     [6,8,0,0,7,0,0,9,0],
    #     [1,9,0,0,0,4,5,0,0],
    #     [8,2,0,1,0,0,0,4,0],
    #     [0,0,4,6,0,2,9,0,0],
    #     [0,5,0,0,0,3,0,2,8],
    #     [0,0,9,3,0,0,0,7,4],
    #     [0,4,0,0,5,0,0,3,6],
    #     [7,0,3,0,1,8,0,0,0]]
    # print(find_unfilled(data))
    if solve_sudoku(data):
        output(data)
    else:
        print("Sudoku cannot be solved")
    # print(col_check(data,1,6))
    # print(row_check(data,1,0))
    # print(subgrid_check(data,1,0,6))
    # if result == False:
    #     print("Sudoku cannot be solved")


# data = keyboard_input()
# solve_main(data)
    
# test cases 
# 726493815
# 315728946
# 489651237
# 852147693
# 673985124
# 941362758
# 194836572
# 567214389
# 238579460

# 706003000
# 000000000
# 409000000
# 050007093
# 673085020
# 940000050
# 100006002
# 007200380
# 230570461

# 900000000
# 000000000
# 000000000
# 000000000
# 000000000
# 000000000
# 000000000
# 000000000
# 000000000
