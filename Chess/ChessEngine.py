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
            ["--", "--", "--", "bp", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]
        self.moveFunctions = {"p": self.getPawnMoves, "R": self.getRookMoves, "N": self.getKnightMoves, "B": self.getBishopMoves, "Q": self.getQueenMoves, "K": self.getKingMoves}

        self.whiteToMove = True
        self.moveLog = []

    def makeMove(self, move):
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.moveLog.append(move) # Log move so i can undo later
        self.whiteToMove = not self.whiteToMove # Switch turn


    def undoMove(self):
        if len(self.moveLog) != 0:
            move = self.moveLog.pop()
            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board[move.endRow][move.endCol] = move.pieceCaptured
            self.whiteToMove = not self.whiteToMove

    """
    All moves considering checks
    """
    def getValidMoves(self):
        return self.getAllPossibleMoves()


    """
    All moves without considering checks
    """
    def getAllPossibleMoves(self):
        moves = []
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                turn = self.board[row][col][0]
                if (turn == "w" and self.whiteToMove) or (turn == "b" and not self.whiteToMove):
                    piece = self.board[row][col][1]
                    self.moveFunctions[piece](row, col, moves)
        return moves
                    

    """
    Get all the pawn moves for the pawn located at row, col and add these moves to the list
    """
    def getPawnMoves(self, row, col, moves):
        if self.whiteToMove:
            if self.board[row-1][col] == "--":
                moves.append(Move((row, col), (row-1, col), self.board))
                if row == 6 and self.board[row-2][col] == "--": 
                    moves.append(Move((row, col), (row-2, col), self.board))
            if col-1 >= 0: # Capture to the left
                if self.board[row-1][col-1][0] == "b":
                    moves.append(Move((row, col), (row-1, col-1), self.board))
            if col+1 <= 7: # Captures to the right
                if self.board[row-1][col+1][0] == "b": 
                    moves.append(Move((row, col), (row-1, col+1), self.board))


    def getRookMoves(self, row, col, moves):
        pass

    def getKnightMoves(self, row, col, moves):
        pass

    def getBishopMoves(self, row, col, moves):
        pass
    
    def getQueenMoves(self, row, col, moves):
        pass

    def getKingMoves(self, row, col, moves):
        pass


class Move():
    # Maps keys to values
    # key : value
    # k = key, v = value
    ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4,
                   "5": 3, "6": 2, "7": 1, "8": 0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()}
    filesToCols = {"a": 0, "b": 1, "c": 2, "d": 3,
                   "e": 4, "f": 5, "g": 6, "h": 7}
    colsToFiles = {v: k for k, v in filesToCols.items()}

    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]
        self.moveID = self.startRow * 1000 + self.startCol * 100 + self.endRow * 10 + self.endCol
        print(self.moveID)

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.moveID == other.moveID
        return False
    

    def getChessNotation(self):
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)

    def getRankFile(self, row, col):
        return self.colsToFiles[col] + self.rowsToRanks[row]