# D104 Python: Beyond the Basics
# File: maze_skeleton.py
# A text-based maze game:
# The symbol 'P' represents the player
# The symbol '#' represents wall, which the player cannot move to
# The symbol 'E' represents the exit where the player has to move 
#                           to in order to win the game

# print_maze() prints the maze
def print_maze(maze_board):
    for i in maze_board:
        for j in i:
            print(j, end='')
        print()

# find_symbol_position() returns the row and column numbers
# of the given symbol in the maze
def find_symbol_position(maze_board, symbol_char='P'):
    # TODO 1: Complete find_symbol_position() to find where 
    #       the given character, symbol_char, is in the maze
    #       Return the corresponding row number and column number
    for i in range(len(maze_board)):
        for j in range(len(maze_board[i])):
            if maze_board[i][j] == symbol_char:
                return (i,j)


# is_valid_move() checks if moving the player with the given direction 
# is valid or not (i.e. not enountering wall)
def is_valid_move(maze_board, row, col, direction):
    # check move up
    if direction == 'w':
        if (row - 1) >= 0 and maze_board[row-1][col] != '#':
            return True
    # check move down
    elif direction == 's':
        if (row + 1) < len(maze_board) and maze_board[row+1][col] != '#':
            return True
    # check move left
    elif direction == 'a':
        if (col - 1) >= 0 and maze_board[row][col-1] != '#':
            return True
    # check move right
    elif direction == 'd':
        if (col + 1) < len(maze_board[0]) and maze_board[row][col+1] != '#':
            return True
    return False

# update_maze() moves the player in the maze and
#  returns the player's updated row and col number
def update_maze(maze_board, row, col, direction):
    # set the current position to space (' ')
    maze_board[row][col] = ' '

    # move up
    if direction == 'w':
        row -= 1
        
    # TODO 2: add the code for move down ('s')
    elif direction == 's':
        row += 1

    # move left
    elif direction == 'a':
        col -= 1

    # TODO 3: add the code for move right ('d')
    elif direction == 'd':
        col += 1

    # TODO 4: assign 'P' to the updated position
    maze_board[row][col] = 'P'

    return (row, col)

# main loop of the game
print("Welcome to the maze game!")
print("You are trapped in this maze ('P'), let's find the exit ('E')!")

# initialize the maze
maze = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', 'P', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', '#', ' ', '#', '#', ' ', '#', '#', '#', '#'],
        ['#', ' ', '#', '#', ' ', ' ', ' ', ' ', '#', ' ', '#'],
        ['#', ' ', ' ', '#', ' ', '#', ' ', ' ', '#', ' ', '#'],
        ['#', ' ', '#', '#', ' ', ' ', '#', ' ', '#', ' ', '#'],
        ['#', '#', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', 'E', '#']]

# find the player's initial position (row & col numbers)
(player_row, player_col) = find_symbol_position(maze)
# find the position of the exit (row & col numbers)
(exit_row, exit_col) = find_symbol_position(maze, 'E')

# initialize the game status
playing = True

while playing:
    # print the maze
    print_maze(maze)
    # get the next move from the player
    move_direction = input("Enter your move\n('w' to move up, 's' to move down,\n'a' to move left, 'd' to move right): ")

    # check if the move is valid
    if is_valid_move(maze, player_row, player_col, move_direction):

        # TODO 5: Call the function update_maze and get the player's updated position (row & column number)
        (player_row, player_col) = update_maze(maze, player_row, player_col, move_direction)
        
        # check if the player has reached the exit or not
        if player_row == exit_row and player_col == exit_col:
            print("Congratulatioins! You win!")
            playing = False
    else:
        print("The move is invalid!")

# end of program