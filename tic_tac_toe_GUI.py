"""tic tac toe + fileIO + GUI"""
import tkinter as tk
import ast

# We set the player to Player 1 and switch between the two players
# player 1 ID is 1, player 2 ID is 2
player = 1

# Variables that will help us decide when the game is finished    
running = True  
filename = "saved_game.txt"


def box_pressed(symbol, row, col):
    global player, running 
    if player == 1:    
        #"Player 1's chance"
        mark = 'X'    
    else:    
        #"Player 2's chance"
        mark = 'O'
     # Check if the position is empty or not
    if symbol == ' ' and running == True:
         # update the position to record the mark
        board_status[row][col][0] = mark
        filled_box = tk.Button(gui, text = mark, fg='black', bg='grey', height=2, width=5)
        filled_box.grid(row=row,column=col)
        #Display draw or win
        if check_draw() == True:
            tk.messagebox.showinfo("Game Draw", "Game_Draw!!!")
            running = False
        elif check_win(mark) == True:
            tk.messagebox.showinfo("Win", f"Congratulations! player {player} wins!!!")
            running = False 
        #change player
        if mark == 'X':
            player = 2
        else:
            player = 1
  

def quit_clicked():
    string_status = str(board_status)
    with open(filename, 'w') as output_file:
        output_file.write(str(player) + "\n") #store which players' turn
        output_file.write(string_status) #store the board_status as a string
    gui.destroy()


#Main loop of the tic-tac-toe game, runs as long as running is True
def check_win(mark):
    """Check for any winning conditions, returns True if winning condition is met"""
    # For each of the position, check if any of the wining conditions are true.
    for each_row in board_status:
        for each_col in each_row:
            # Step 1: Check Horizontal Winning Conditions
            count = 0
            (temp_row, temp_col) = (each_col[1], each_col[2])
            while temp_col < 5:
                if board_status[temp_row][temp_col][0] == mark:
                    count += 1
                else:
                    break
                temp_col += 1
            if count == 4:
                return True
                break

            # Step 2: Check Vertical Winning Condition
            count = 0
            (temp_row, temp_col) = (each_col[1], each_col[2])
            while temp_row < 5:
                if board_status[temp_row][temp_col][0] == mark:
                    count += 1
                else:
                    break
                temp_row += 1
            if count == 4:
                return True
                break

            # Step 3: Check Diagonal Winning Condition
            count = 0
            (temp_row, temp_col) = (each_col[1], each_col[2])
            while temp_row < 5 and temp_col < 5:
                if board_status[temp_row][temp_col][0] == mark:
                    count += 1
                else:
                    break
                temp_row += 1
                temp_col += 1
            if count == 4:
                return True
                break

            # Step 4: Check Anti-diagonal Winning Condition    
            # e.g. if row is 0, col is 3,
            #      board[0][3] and board[1][2], board[2][1] and board[3][0] are the same, etc.
            count = 0
            (temp_row, temp_col) = (each_col[1], each_col[2])
            while temp_row < 5 and temp_col >= 0:
                if board_status[temp_row][temp_col][0] == mark:
                    count += 1
                else:
                    break
                temp_row += 1
                temp_col -= 1
            if count == 4:
                return True
                break


        # Step 5: Check Draw Condition
        # Check if all positions in board are filled, i.e. no unfilled position
def check_draw():
    """Check for Draw Condition, returns True if draw and returns
    False if there is still unfilled position"""
    for each_row in board_status:
        for each_col in each_row:
            if board_status[each_col[1]][each_col[2]][0] == " ":
                return False
    return True

# set up the TKinter window
gui = tk.Tk()
gui.configure(background = "white")
gui.title("5x5 Tic Tac Toe")
gui.geometry("525x300")


button_board = [
    [[" ", 0,0], [" ", 0,1], [" ", 0,2], [" ", 0,3], [" ", 0,4]],
    [[" ", 1,0], [" ", 1,1], [" ", 1,2], [" ", 1,3], [" ", 1,4]],
    [[" ", 2,0], [" ", 2,1], [" ", 2,2], [" ", 2,3], [" ", 2,4]],
    [[" ", 3,0], [" ", 3,1], [" ", 3,2], [" ", 3,3], [" ", 3,4]],
    [[" ", 4,0], [" ", 4,1], [" ", 4,2], [" ", 4,3], [" ", 4,4]]
    ]

board_status = [
    [[" ", 0,0], [" ", 0,1], [" ", 0,2], [" ", 0,3], [" ", 0,4]],
    [[" ", 1,0], [" ", 1,1], [" ", 1,2], [" ", 1,3], [" ", 1,4]],
    [[" ", 2,0], [" ", 2,1], [" ", 2,2], [" ", 2,3], [" ", 2,4]],
    [[" ", 3,0], [" ", 3,1], [" ", 3,2], [" ", 3,3], [" ", 3,4]],
    [[" ", 4,0], [" ", 4,1], [" ", 4,2], [" ", 4,3], [" ", 4,4]]
    ]


msg1 = tk.messagebox.askquestion("New Game?", "Do you want to load the previous unfinished game?", )
if msg1 == "yes":
    with open(filename, 'r') as input_file:
        lines = input_file.readlines()
        if lines != " ":
            player = int(lines[0].strip())
            previous_game_str = lines[1]
            previous_game = ast.literal_eval(previous_game_str) #turn string back to list
            button_board = board_status = previous_game


for i in button_board:
    for [symbol, row, col] in i:
        new_button = tk.Button(gui, text=symbol, fg='black', bg='grey',
                           command=lambda argument=symbol, box_row=row, box_col=col: box_pressed(argument, box_row, box_col),
                           height=2, width=5)
        new_button.grid(row=row,column=col)

quit_button = tk.Button(gui, text="Quit and Save",
                        command=lambda: quit_clicked(), height=5, width=10) 

intro = tk.Label(gui, text="To win the 5x5 Tic-Tac-Toe, you need to get 4 in a row\n player 1: X       player 2: O")
                 

quit_button.grid(row=7,column=7)
intro.grid(row=0, column=7)


gui.mainloop()