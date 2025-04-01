import chess

# Create a board
board = chess.Board()

# Make moves
board.push_san("e4")
board.push_san("c5")
board.push_san("Nf3")
board.push_san("d6")

# Print the board
print(board)

# Get legal moves
print("Legal moves:", list(board.legal_moves))

# Check if a move is legal
move = chess.Move.from_uci("g1c3")
print("Is g1c3 legal?", move in board.legal_moves)

# Get piece at square
piece = board.piece_at(chess.E4)
print("Piece at e4:", piece)

# Check if in check
print("Is in check?", board.is_check())

# Undo a move
board.pop()
print(board)

# Check for game end
print("Is game over?", board.is_game_over())

# Get the FEN
print("FEN:", board.fen())

# Reset the board
board.reset()
print(board)