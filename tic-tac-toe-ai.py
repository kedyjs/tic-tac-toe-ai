board = [' ' for _ in range(9)]  # 3x3 game board

def check_winner(board, player):
    # Check rows, columns and diagonals
    for line in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]:
        if board[line[0]] == board[line[1]] == board[line[2]] == player:
            return True
    return False


def minimax(board, depth, is_maximizing):
    if check_winner(board, 'X'):
        return -1
    if check_winner(board, 'O'):
        return 1
    if ' ' not in board:
        return 0
    
    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

def find_best_move(board):
    best_move = -1
    best_score = -float('inf')
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

def print_board(board):
    for i in range(3):
        print(board[3 * i], '|', board[3 * i + 1], '|', board[3 * i + 2])

def main():
    print("Welcome to XOX game")
    print_board(board)
    while ' ' in board:
        if not check_winner(board, 'O'):
            player_move = int(input("Please make your move (0-8): "))
            if board[player_move] == ' ':
                board[player_move] = 'X'
                print_board(board)
            else:
                print("Invalid move, try again!")
        else:
            print("O win!")
            break
        if not check_winner(board, 'X'):
            if ' ' in board:
                move = find_best_move(board)
                if move == -1:
                    print("Equal!")
                    break
                board[move] = 'O'
                print_board(board)
        else:
            print("X win!")
            break
    if not check_winner(board, 'O') and not check_winner(board, 'X'):
        print("Equal!")

if __name__ == "__main__":
    main()
