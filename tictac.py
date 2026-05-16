import math


board = [' ' for _ in range(9)]

def check_winner(b):
  
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    

    for combo in win_combinations:
        if b[combo[0]] == b[combo[1]] == b[combo[2]] != ' ':
            return b[combo[0]] # Return 'X' or 'O'
            
    
    if ' ' not in b:
        return "Draw"
        
    return None

def minimax(is_maxing):
    res = check_winner(board)
    if res == 'X': return 1 
    if res == 'O': return -1 
    if res == 'Draw': return 0
    
    if is_maxing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X' 
                score = minimax(False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O' 
                score = minimax(True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

def best_move():
    best_val = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            score = minimax(False)
            board[i] = ' '
            if score > best_val:
                best_val = score
                move = i
    return move

def display_board():
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6: print("---------")

def play():
    print("Welcome to Tic-Tac-Toe (AI uses X, You use O)")
    while True:
        display_board()
        
        # User Input
        try:
            user_choice = int(input("Enter position (0-8): "))
            if board[user_choice] != ' ':
                print("Position taken! Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Enter 0-8.")
            continue
            
        board[user_choice] = 'O'
        
        if check_winner(board): break
        
        # AI Move
        print("\nAI is thinking...")
        move = best_move()
        if move != -1:
            board[move] = 'X'
            
        if check_winner(board): break

    display_board()
    result = check_winner(board)
    if result == "Draw":
        print("It's a Draw!")
    else:
        print(f"Result: {result} wins!")

# Start the game
if __name__ == "__main__":
    play()