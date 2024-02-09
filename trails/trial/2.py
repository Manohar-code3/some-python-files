def is_valid_square(aquare,board):
    return 1<= square <= len(board) **2
def play_game(board,dice_inputs):
    current_square=board[0][0]
    snakes=0
    ladders=0

    for die_input in dice_inputs:
        next_square =current_square +die_input

        if is_valid_square(next_square,board):
            current_square = next_square

            if board[current_square// len(board)][current_square % len(board)]=="E":
                return "Possible", snakes,ladders,current_square
            elif board[current_square// len(board)][current_square % len(board)].startswith("S("):
                snakes+=1
                current_square=int(board[current_square// len(board)][current_square % len(board)][2:-1])
            elif board[current_square// len(board)][current_square % len(board)].startswith("L("):
                ladders+=1
                current_square=int(board[current_square// len(board)][current_square % len(board)][2:-1])
        else:
            return "Not possible", snakes, ladders, current_square
board=[list(input().split()) for _ in range(10)]

dice_inputs=list(map(int,input().split()))

result,snakes, ladders, square=play_game(board,dice_inputs)
print(f"{result} {snakes}:{ladders} {square}")
            