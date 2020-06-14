import tkinter as tk
from tkinter.font import Font
import chess

#helv36 = Font(family="Helvetica",size=36,weight="bold")

board = chess.STARTING_BOARD_FEN.replace('8', '').replace('/', '')
print(board)

wp = ['♔', '♕', '♖', '♗', '♘', '♙']
bp = ['♚', '♛', '♜', '♝', '♞', '♟']
board = [ ['']*8 for _ in range(8) ]
board[0] = [bp[2], bp[4], bp[3], bp[1], bp[0], bp[3], bp[4], bp[2]]
board[1] = [bp[5]] * 8
board[6] = [wp[5]] * 8
board[7] = [wp[2], wp[4], wp[3], wp[1], wp[0], wp[3], wp[4], wp[2]]
print(board)
counter = 0

root = tk.Tk()

saved = ''
saved_location = (-1, -1)

def on_click(i,j,event):
    piece = board[i][j]
    #global saved

    if saved_location != (-1, -1):
        if piece != '':
            board[i][j] = saved
            saved = ''

    # global counter
    # if counter % 2:
    #     color = "white"
    #     piece = '♘'
    # else:
    #     color = "black"
    #     piece = '♞'
    event.widget.config(text=piece)
    # board[i][j] = color
    # counter += 1

for i,row in enumerate(board):
    for j,column in enumerate(row):
        if i % 2 == 0 and j % 2 == 0:
            color = "grey"
        elif i%2 == 0 and j %2 != 0:
            color= "lightgrey"
        elif i%2 != 0 and j%2 == 0:
            color="lightgrey"
        else:
            color = "grey"
        L = tk.Button(root,text=board[i][j],bg=color, height=2, width=5, font=("Times New Roman", 24))
        L.grid(row=i,column=j)
        L.bind('<Button-1>',lambda e,i=i,j=j: on_click(i,j,e))

root.mainloop()