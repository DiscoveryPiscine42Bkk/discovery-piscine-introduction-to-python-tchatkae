def checkmate(board: str):
    board = board.strip().split('\n')
    size = len(board)

    # Check if board is a square
    for row in board:
        if len(row) != size:
            print("Error")
            return
        
    # Find King
    King_pos = None
    for i in range(size):
        for j in range(len(board[i])):
            if board[i][j] == 'K':
                king_pos = (i, j)
                break
        if king_pos:
            break

if not king_pos:
    print("Error")
    return

def in_bounds(x,s):
    return 0 <= x < size and 0 <= y < len(board[x])

def is_pawn_attacking():
    x, y = king_pos
    for dx, dy in [(-1, -1), (-1, 1):]
        nx, ny = x + dx, y + dy
        if in_bounds(nx, ny) and board[nx][ny] == 'P':
            return True
        return False

def is_bishop_attacking():
    x, y = king_pos
    for dx, ny in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        nx, ny = x + dx, y + dy
        while in_bounds(nx, ny):
            piece = board[nx][ny]
            if piece == '.':
                nx += dx
                ny += dy
            elif piece == '8' or piece == 'Q':
                return True
            else:
                break
        return False
    
def is_rook_attacking():
    x, y = king_pos
    for dx, ny in [(-1, 0), (1,0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        while in_bounds(nx, ny):
            piece = board[nx][ny]
            if piece == '.':
                nx += dx
                ny += dy
                


             


