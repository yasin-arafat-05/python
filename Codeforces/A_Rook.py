def rook_moves(square):
    col, row = square[0], int(square[1])
    horizontal_moves = [f"{chr(i)}{row}" for i in range(ord('a'), ord('i')) if chr(i) != col]
    vertical_moves = [f"{col}{i}" for i in range(1, 9) if i != row]
    all_moves = horizontal_moves + vertical_moves
    return all_moves

t = int(input())
for _ in range(t):
    position = input().strip()
    moves = rook_moves(position)
    for move in moves:
        print(move)
