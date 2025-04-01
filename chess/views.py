import importlib

pychess = importlib.import_module("chess")

from django.shortcuts import render, redirect
from django import forms

# A simple form for a chess move (UCI format, e.g., "e2e4")
class MoveForm(forms.Form):
    move = forms.CharField(
        label="Enter your move (UCI format, e.g., 'e2e4')",
        max_length=10,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

def get_board(request):
    """
    Retrieve the current board from the session.
    If not present, initialize a new board.
    """
    fen = request.session.get('board_fen')
    if fen:
        return pychess.Board(fen)
    else:
        board = pychess.Board()
        request.session['board_fen'] = board.fen()
        return board

def index(request):
    """
    Display the current chess board, list legal moves,
    and show the form to submit a move.
    """
    board = get_board(request)
    form = MoveForm()
    context = {
        'board_str': str(board),
        'legal_moves': [move.uci() for move in board.legal_moves],
        'form': form,
    }
    return render(request, 'index.html', context)

def make_move(request):
    """
    Process the submitted move and update the board.
    """
    board = get_board(request)
    if request.method == 'POST':
        form = MoveForm(request.POST)
        if form.is_valid():
            move_input = form.cleaned_data['move']
            move = pychess.Move.from_uci(move_input)
            if move in board.legal_moves:
                board.push(move)
                request.session['board_fen'] = board.fen()
    return redirect('index')
