# D104 Summer 2022
# Tic-Tac-Toe 5x5

print("To win in Tic-Tac-Toe 5x5, you need to get 4 in a row!")

# Create a 2D board and fill it with ' '
board = [[' ',' ',' ',' ',' '], [' ',' ',' ',' ',' '], [' ',' ',' ',' ',' '],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ']]

# We set the player to Player 1 and switch between the two players
# player 1 ID is 1, player 2 ID is 2
player = 1

# Variables that will help us decide when the game is finished 
win = False   
draw = False    
running = True  
filename = "game.txt"

# Decide whether to start a new game or load a previous one
print("Do you want to load the previous unfinished game? ")
resume_game = input("Enter 'Y' to load a previous game or 'N' to start a new game: ")

if resume_game == 'y' or resume_game == 'Y':
    with open(filename, 'r') as input_file:
        lines = input_file.readlines()
        player = int(lines[0].strip())
        # TODO 2: Complete the code to read the game board from 
        #       the file to the variable, board (a 2d list)
        # Step: read each of the line and store it as a row in board
        for i in range(1, len(lines)):
            print(i)
            board[i-1] = list(lines[i][0:5])
            for j in range(5):
                board[i-1][j]=lines[i][j]

# Draw the board
# We use "%s" %(board[i][j]) to print strings while maintaining the formatting
print("   | 0 | 1 | 2 | 3 | 4 |")    
print("---|---|---|---|---|---|")    
for i in range(5):
    print(" %s | %s | %s | %s | %s | %s |" % (i, board[i][0], board[i][1], board[i][2], board[i][3], board[i][4]))
    print("---|---|---|---|---|---|")    

#Main loop of the tic-tac-toe game, runs as long as running is True
while (running == True):

    #Player 1's turn if odd otherwise Player 2's turn
    if player == 1:    
        print("Player 1's chance")
        mark = 'X'    
    else:    
        print("Player 2's chance")
        mark = 'O'
        
    #Enter the user's choice and change it to an integer 
    row_choice = int(input("Enter the row between [0-4] where you want to mark : ")) 
    column_choice = int(input("Enter the column between [0-4] where you want to mark : ")) 

    # Check if the position is empty or not
    if board[row_choice][column_choice] == ' ':
        # update the position to record the mark
        board[row_choice][column_choice] = mark

        # Draw the board
        # We use "%s" %(board[i][j]) to print strings while maintaining the formatting
        print("   | 0 | 1 | 2 | 3 | 4 |")    
        print("---|---|---|---|---|---|")    
        for i in range(5):
            print(" %s | %s | %s | %s | %s | %s |" % (i, board[i][0], board[i][1], board[i][2], board[i][3], board[i][4]))
            print("---|---|---|---|---|---|")    

        # For each of the position, check if any of the wining conditions are true.
        for row in range(5):
            for col in range(5):
                # Step 1: Check Horizontal Winning Conditions and set the variable, win, to True
                # by counting the number of same mark positions horizontally
                # e.g. row is 0 and col is 0,
                #      board[0][0] and board[0][1], board[0][2] and board[0][3] are the same as mark, 
                #      count is 4, so win is set to True
                count = 0
                (temp_row, temp_col) = (row, col)
                while temp_col < 5:
                    if board[temp_row][temp_col] == mark:
                        count = count + 1
                    else:
                        break
                    temp_col = temp_col + 1
                if count == 4:
                    win = True
                    break

                # Step 2: Check Vertical Winning Condition and set the variable, win, to True 
                # e.g. board[0][0] and board[1][0], board[2][0] and board[3][0] are the same as mark, etc.
                count = 0
                (temp_row, temp_col) = (row, col)
                while temp_row < 5:
                    if board[temp_row][temp_col] == mark:
                        count = count + 1
                    else:
                        break
                    temp_row = temp_row + 1
                if count == 4:
                    win = True
                    break

                # Step 3: Check Diagonal Winning Condition and set the variable, win, to True    
                # e.g. board[0][0] and board[1][1], board[2][2] and board[3][3] are the same, etc.
                count = 0
                (temp_row, temp_col) = (row, col)
                while temp_row < 5 and temp_col < 5:
                    if board[temp_row][temp_col] == mark:
                        count = count + 1
                    else:
                        break
                    temp_row = temp_row + 1
                    temp_col = temp_col + 1
                if count == 4:
                    win = True
                    break

                # Step 4: Check Anti-diagonal Winning Condition and set the variable, win, to True    
                # e.g. if row is 0, col is 3,
                #      board[0][3] and board[1][2], board[2][1] and board[3][0] are the same, etc.
                count = 0
                (temp_row, temp_col) = (row, col)
                while temp_row < 5 and temp_col >= 0:
                    if board[temp_row][temp_col] == mark:
                        count = count + 1
                    else:
                        break
                    temp_row = temp_row + 1
                    temp_col = temp_col - 1
                if count == 4:
                    win = True
                    break

            if win == True:
                break

        # Step 5: Match Tie or Draw Condition and set the variable, draw, to True
        # TODO 1: 
        # Step 1: Check if all positions in board are filled, i.e. no unfilled position
        a = True
        for row in range(5):
            for col in range(5):
                if board[row][col] == " ":
                    a = False
        # Step 2: If there is no unfilled position, set the variable, draw, to True
        if a != False:
            draw = True


        # If draw is true or win is true
        if draw == True:
            print("Game draw!")
            running = False
        elif win == True:

            print("Congratulations! Player %d Won" % player)    
            running = False

        if player == 1:
            player = 2
        else:
            player = 1
    
    command=input("Enter 'C' to continue or 'Q' to quit and save the current game: ")
    if command == 'Q' or command == 'q':

        # TODO 3: Complete the code to save the game
        # Step 1: open the file with filename to write (overwrite)
        # Step 2: Save the next player information in the 1st line 
        # Step 3: Save each row of board into each line
        with open(filename, 'w') as output_file:
            output_file.write(str(player)+'\n')
            for each_row in board:
                for each_pos in each_row:
                    output_file.write(each_pos)
                output_file.write("\n")

        running = False