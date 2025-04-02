import chess
import chess.pgn

# Define a sequence of moves in SAN notation.
# (Adjust the move sequence to ensure every move is legal.)
moves = [
    "e4",  # White: Pawn to e4
    "c5",  # Black: Pawn to c5
    "f3",  # White: Pawn to f3
    "d6",  # Black: Pawn to d6
    "Nc3",  # White: Knight to c3
    "Nf6",  # Black: Knight to f6
    "d4",  # White: Pawn to d4
    "cxd4",  # Black: Pawn takes on d4
    "Nxd4",  # White: Knight takes on d4 (attempted move, may be illegal)
    "Nxd4",  # Black: Knight recaptures on d4 (attempted move)
    "Qxd4",  # White: Queen takes on d4
    "e6",  # Black: Pawn to e6
]

board = chess.Board()

# Apply moves one by one, catching errors if a move is illegal.
for move in moves:
    try:
        board.push_san(move)
    except Exception as e:
        print(f"Error applying move {move}: {e}")
        break

# Display the current board position.
print("Current board position:")
print(board)

# List and display all legal moves.
legal_moves = list(board.legal_moves)
print("\nLegal moves:")
for move in legal_moves:
    print(move)

# List and display all pseudo-legal moves.
pseudo_legal_moves = list(board.pseudo_legal_moves)
print("\nPseudo-legal moves (includes moves that may leave king in check):")
for move in pseudo_legal_moves:
    print(move)

# Check if a specific move is legal (using UCI format)
move_to_check = chess.Move.from_uci("g1f3")
print("\nIs g1f3 legal?", move_to_check in board.legal_moves)

# Get the piece at e4 (using chess.E4 constant) and print it
piece_e4 = board.piece_at(chess.E4)
print("\nPiece at e4:", piece_e4)

# Check the board status
print("\nBoard status:")
print("Is in check?", board.is_check())
print("Is checkmate?", board.is_checkmate())
print("Is stalemate?", board.is_stalemate())
print("Is game over?", board.is_game_over())

# Print the move history using a temporary board
print("\nMove history:")
temp_board = chess.Board()
for i, move in enumerate(board.move_stack, start=1):
    san_move = temp_board.san(move)
    print(f"Move {i}: {san_move}")
    temp_board.push(move)

# Undo the last move and show the updated board
board.pop()
print("\nBoard after undoing the last move:")
print(board)

# Get and print the FEN (Forsyth-Edwards Notation) for the current position
fen = board.fen()
print("\nFEN:", fen)

# Check if the game is over and, if so, display the outcome
if board.is_game_over():
    outcome = board.outcome()
    print("Outcome:", outcome)
else:
    print("The game is still in progress.")

# Create a PGN representation of the game so far.
game = chess.pgn.Game()
node = game
temp_board = chess.Board()
for move in board.move_stack:
    node = node.add_variation(move)
    temp_board.push(move)
print("\nPGN representation of the current game:")
print(game)

# Set up a new board from a FEN string.
new_fen = "rnbqkbnr/ppp2ppp/4p3/3p4/3P4/2N5/PPP1PPPP/R1BQKBNR w KQkq - 0 3"
board.set_fen(new_fen)
print("\nBoard set from new FEN:")
print(board)

# Finally, reset the board to the starting position.
board.reset()
print("\nBoard after reset:")
print(board)
