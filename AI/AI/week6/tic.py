import os

def clear():
    if os.name=="nt":
        os.system("cls")
    else:
        os.system("clear")
def print_table(board):
    clear()
    print(f"{board[0]}  | {board[1]} | {board[2]} ")
    print("___|___|___")
    print(f"{board[3]}  | {board[4]} | {board[5]} ")
    print("___|___|____")
    print(f"{board[6]}  | {board[7]} | {board[8]} ")

def getmoves(inputs):
    while True:
        move=int(input(f"{inputs} at enter the number"))
def check_winner(board):
    for i in range(3):
        row=i*3
        if board[row]==board[row+1]==board[row+2]:
            return True
        col=i
        if board[col]==board[col+3]==board[col+6]:
            return True
        if board[0]==board[4]==board[8]:
            return True
        if board[2]==board[4]==board[6]:
            return True
def play_game():
    inputs=["X","O"]
    player=inputs[0]
    agent=inputs[1]
    









