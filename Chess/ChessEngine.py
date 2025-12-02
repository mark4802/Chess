"""
This class is responsible for storing all the informatuion about the current state of a chess game. It will also be responsible for determining the valid moves at the current state. It will also keep a move log.
"""

class GameState():
    def __init__(self):
        # The board is an 8x8 2d list, each element of the list has 2 characters. 
        # The first character represents the color of the piece
        # The second character represents the type of piece
        # "--" represents an empty space 
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]
        self.whiteToMove = True
        self.moveLog = []