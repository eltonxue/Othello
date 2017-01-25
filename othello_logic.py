# othello_logic.py ICS 32 Lab. Elton Xue 52611936

###########
# Players #
###########

NONE = 0
BLACK = 1
WHITE = 2

###########
# Classes #
###########

class GameState:
    def __init__(self, rows: int, columns: int, start_arrangement: str, first_turn: str):
        '''Initializes the GameState of Othello by assigning the number of rows and columns
        the user asks for and building the new board, the starting arragement of the first four pieces,
        and the player who makes the first turn into variables inside the class'''
        self._rows = rows
        self._columns = columns
        self._board = _new_game_board(self._rows, self._columns, start_arrangement)
        self._turn = 0
        if first_turn == 'B':
            self._turn += BLACK
        else:
            self._turn += WHITE

    def make_move(self, row: int, col: int) -> bool:
        '''Takes the row and column the user makes and checks whether or not
        that move is valid by checking all the cells around their move. If
        the move is invalid, it returns False. If the move is valid, it changes
        the cell to that player's piece and returns True'''
        row -= 1
        col -= 1

        EMPTY = (self._board[col][row] == 0)
        
        OPPONENT_UP = (self._board[col][row - 1] == _opposite_turn(self._turn) and _OPPONENT_UP_VALID(row, col, self._board, self._turn))
        OPPONENT_DOWN = (self._board[col][row + 1] == _opposite_turn(self._turn) and _OPPONENT_DOWN_VALID(row, self._rows, col, self._board, self._turn))
        OPPONENT_LEFT = (self._board[col + 1][row] == _opposite_turn(self._turn) and _OPPONENT_LEFT_VALID(row, col, self._columns, self._board, self._turn))
        OPPONENT_RIGHT = (self._board[col - 1][row] == _opposite_turn(self._turn) and _OPPONENT_RIGHT_VALID(row, col, self._board, self._turn))
        OPPONENT_UP_LEFT = (self._board[col - 1][row - 1] == _opposite_turn(self._turn) and _OPPONENT_UP_LEFT_VALID(row, col, self._board, self._turn))
        OPPONENT_UP_RIGHT = (self._board[col + 1][row - 1] == _opposite_turn(self._turn) and _OPPONENT_UP_RIGHT_VALID(row, col, self._columns, self._board, self._turn))
        OPPONENT_DOWN_LEFT = (self._board[col - 1][row + 1] == _opposite_turn(self._turn) and _OPPONENT_DOWN_LEFT_VALID(row, self._rows, col, self._board, self._turn))
        OPPONENT_DOWN_RIGHT = (self._board[col + 1][row + 1] == _opposite_turn(self._turn) and _OPPONENT_DOWN_RIGHT_VALID(row, self._rows, col, self._columns, self._board, self._turn))
        
        if EMPTY and (OPPONENT_UP or OPPONENT_DOWN or OPPONENT_LEFT or OPPONENT_RIGHT or OPPONENT_UP_LEFT or OPPONENT_UP_RIGHT or OPPONENT_DOWN_LEFT or OPPONENT_DOWN_RIGHT):
            
            opponent_piece = _opposite_turn(self._turn)
            
            while opponent_piece == _opposite_turn(self._turn):
                if OPPONENT_UP:
                    for minus_row in reversed(range(row)):
                        if self._board[col][minus_row] == _opposite_turn(self._turn):
                            self._board[col][minus_row] = self._turn
                        else:
                            opponent_piece = self._turn
                            break
                if OPPONENT_DOWN:
                    for plus_row in range(row + 1, self._rows):
                        if self._board[col][plus_row] == _opposite_turn(self._turn):
                            self._board[col][plus_row] = self._turn
                        else:
                            opponent_piece = self._turn
                            break
                if OPPONENT_LEFT:
                    for plus_col in range(col + 1, self._columns):
                        if self._board[plus_col][row] == _opposite_turn(self._turn):
                            self._board[plus_col][row] = self._turn
                        else:
                            opponent_piece = self._turn
                            break
                if OPPONENT_RIGHT:
                    for minus_col in reversed(range(col)):
                        if self._board[minus_col][row] == _opposite_turn(self._turn):
                            self._board[minus_col][row] = self._turn
                        else:
                            opponent_piece = self._turn
                            break
                if OPPONENT_UP_LEFT:
                    for _col, _row in zip(reversed(range(col)), reversed(range(row))):
                        if self._board[_col][_row] == _opposite_turn(self._turn):
                            self._board[_col][_row] = self._turn
                        else:
                            opponent_piece = self._turn
                            break
                if OPPONENT_DOWN_RIGHT:
                    for _col, _row in zip(range(col + 1, self._columns), range(row + 1, self._rows)):
                        if self._board[_col][_row] == _opposite_turn(self._turn):
                            self._board[_col][_row] = self._turn
                        else:
                            opponent_piece = self._turn
                            break
                if OPPONENT_UP_RIGHT:
                    for _col, _row in zip(range(col + 1, self._columns), reversed(range(row))):
                        if self._board[_col][_row] == _opposite_turn(self._turn):
                            self._board[_col][_row] = self._turn
                        else:
                            opponent_piece = self._turn
                            break
                if OPPONENT_DOWN_LEFT:
                    for _col, _row in zip(reversed(range(col)), range(row + 1, self._rows)):
                        if self._board[_col][_row] == _opposite_turn(self._turn):
                            self._board[_col][_row] = self._turn
                        else:
                            opponent_piece = self._turn
                            break
                self._board[col][row] = self._turn
            self._turn = _opposite_turn(self._turn)
            return True
        else:
            return False

    def turn(self) -> int:
        '''Returns the user of the current turn'''
        return self._turn

    def board(self) -> [[int]]:
        '''Returns the current game board'''
        return self._board

    def winner(self, winning_rules: str) -> int:
        '''Returns the winner based on the rules the user's choice at
        the start of the game'''
        if winning_rules == '>':
            if check_black_pieces(self._board) > check_white_pieces(self._board):
                return BLACK
            elif check_white_pieces(self._board) > check_black_pieces(self._board):
                return WHITE
            else:
                return NONE
        else:
            if check_black_pieces(self._board) < check_white_pieces(self._board):
                return BLACK
            elif check_white_pieces(self._board) < check_black_pieces(self._board):
                return WHITE
            else:
                return NONE

    def game_over(self) -> bool:
        '''Checks if there are any possible moves for either sides. If none,
        the game is over and the function returns False''' 
        for row in range(self._rows):
            for col in range(self._columns):
                if _check_possible_move(row, self._rows, col, self._columns, self._board, self._turn):
                    return True
                
        for _row in range(self._rows):
            for _col in range(self._columns):
                if _check_possible_move(_row, self._rows, _col, self._columns, self._board, _opposite_turn(self._turn)):
                    self._turn = _opposite_turn(self._turn)
                    return True
                
        return False

#############
# Functions #
#############

def check_black_pieces(board: [[int]], ) -> int:
    '''Returns the number of black pieces currently on the board'''
    pieces = 0
    for sublist in board:
        for num in sublist:
            if num == BLACK:
                pieces += 1
    return pieces

def check_white_pieces(board: [[int]]) -> int:
    '''Returns the number of white pieces currently on the board'''
    pieces = 0
    for sublist in board:
        for num in sublist:
            if num == WHITE:
                pieces += 1
    return pieces

###########
# Private #
###########

def _check_possible_move(row, max_rows, col, max_columns, board, turn) -> bool:
    '''Check if there is a possible move for the current user's turn'''
    EMPTY = (board[col][row] == 0)
    
    OPPONENT_UP = (board[col][row - 1] == _opposite_turn(turn) and _OPPONENT_UP_VALID(row, col, board, turn))
    OPPONENT_DOWN = (board[col][row + 1] == _opposite_turn(turn) and _OPPONENT_DOWN_VALID(row, max_rows, col, board, turn))
    OPPONENT_LEFT = (board[col + 1][row] == _opposite_turn(turn) and _OPPONENT_LEFT_VALID(row, col, max_columns, board, turn))
    OPPONENT_RIGHT = (board[col - 1][row] == _opposite_turn(turn) and _OPPONENT_RIGHT_VALID(row, col, board, turn))
    OPPONENT_UP_LEFT = (board[col - 1][row - 1] == _opposite_turn(turn) and _OPPONENT_UP_LEFT_VALID(row, col, board, turn))
    OPPONENT_UP_RIGHT = (board[col + 1][row - 1] == _opposite_turn(turn) and _OPPONENT_UP_RIGHT_VALID(row, col, max_columns, board, turn))
    OPPONENT_DOWN_LEFT = (board[col - 1][row + 1] == _opposite_turn(turn) and _OPPONENT_DOWN_LEFT_VALID(row, max_rows, col, board, turn))
    OPPONENT_DOWN_RIGHT = (board[col + 1][row + 1] == _opposite_turn(turn) and _OPPONENT_DOWN_RIGHT_VALID(row, max_rows, col, max_columns, board, turn))

    return (EMPTY and (OPPONENT_UP or OPPONENT_DOWN or OPPONENT_LEFT or OPPONENT_RIGHT or OPPONENT_UP_LEFT or OPPONENT_UP_RIGHT or OPPONENT_DOWN_LEFT or OPPONENT_DOWN_RIGHT))


def _opposite_turn(turn: int) -> int:
    '''Returns the opposite turn of the turn it takes'''
    if turn == BLACK:
        return WHITE
    else:
        return BLACK

def _new_game_board(rows: int, columns: int, start_arrangement: str) -> [[int]]:
    '''Creates the starting game board with the four pieces arranged based on
    what the user enters at the start of the game'''
    board = []

    rows += 2
    columns += 2
    
    middle_row = int(rows / 2) - 2
    middle_col = int(columns / 2) - 2
    
    for col in range(columns):
        board.append([])
        for row in range(rows):
            board[col].append(0)
            
    board[middle_col][middle_row] = _check_start_arrangement(start_arrangement)
    start = board[middle_col][middle_row]
    
    if start == BLACK:
        board[middle_col + 1][middle_row] = WHITE
        board[middle_col][middle_row + 1] = WHITE
        board[middle_col + 1][middle_row + 1] = BLACK
    elif start == WHITE:
        board[middle_col + 1][middle_row] = BLACK
        board[middle_col][middle_row + 1] = BLACK
        board[middle_col + 1][middle_row + 1] = WHITE

    return board

def _check_start_arrangement(start_arrangement: str) -> int:
    '''Checks what the start arrangement is. Whose piece is on the top left'''
    if start_arrangement == 'B':
        return BLACK
    elif start_arrangement == 'W':
        return WHITE

def _OPPONENT_UP_VALID(row: int, col: int, board: [[int]], turn: int) -> bool:
    '''Checks if the move is valid based on if the enemy piece
    above the cell is sandwiched by the current turn's user's piece'''
    for minus_row in reversed(range(row)):
        if board[col][minus_row] == NONE:
            return False
        elif board[col][minus_row] == turn:
            return True
    return False

def _OPPONENT_DOWN_VALID(row: int, max_rows: int, col: int, board: [[int]], turn: int) -> bool:
    '''Checks if the move is valid based on if the enemy piece
    below the cell is sandwiched by the current turn's user's piece'''

    for plus_row in range(row + 1, max_rows):
        if board[col][plus_row] == NONE:
            return False
        elif board[col][plus_row] == turn:
            return True
    return False

def _OPPONENT_LEFT_VALID(row: int, col: int, max_columns: int, board: [[int]], turn: int) -> bool:
    '''Checks if the move is valid based on if the enemy piece
    left of the cell is sandwiched by the current turn's user's piece'''
    for plus_col in range(col + 1, max_columns):
        if board[plus_col][row] == NONE:
            return False
        elif board[plus_col][row] == turn:
            return True
    return False

def _OPPONENT_RIGHT_VALID(row: int, col: int, board: [[int]], turn: int) -> bool:
    '''Checks if the move is valid based on if the enemy piece
    right of the cell is sandwiched by the current turn's user's piece'''
    for minus_col in reversed(range(col)):
        if board[minus_col][row] == NONE:
            return False
        elif board[minus_col][row] == turn:
            return True
    return False

def _OPPONENT_UP_LEFT_VALID(row: int, col: int, board: [[int]], turn: int) -> bool:
    '''Checks if the move is valid based on if the enemy piece
    above and left of the cell is sandwiched by the current turn's user's piece'''
    for _col, _row in zip(reversed(range(col)), reversed(range(row))):
        if board[_col][_row] == NONE:
            return False
        elif board[_col][_row] == turn:
            return True
    return False

def _OPPONENT_UP_RIGHT_VALID(row: int, col: int, max_columns: int, board: [[int]], turn: int) -> bool:
    '''Checks if the move is valid based on if the enemy piece
    above and right of the cell is sandwiched by the current turn's user's piece'''
    for _col, _row in zip(range(col + 1, max_columns), reversed(range(row))):
        if board[_col][_row] == NONE:
            return False
        elif board[_col][_row] == turn:
            return True
    return False

def _OPPONENT_DOWN_LEFT_VALID(row: int, max_rows: int, col: int, board: [[int]], turn: int) -> bool:
    '''Checks if the move is valid based on if the enemy piece
    below and left of the cell is sandwiched by the current turn's user's piece'''
    for _col, _row in zip(reversed(range(col)), range(row + 1, max_rows)):
        if board[_col][_row] == NONE:
            return False
        elif board[_col][_row] == turn:
            return True
    return False
    
def _OPPONENT_DOWN_RIGHT_VALID(row: int, max_rows: int, col: int, max_columns: int, board: [[int]], turn: int) -> bool:
    '''Checks if the move is valid based on if the enemy piece
    below and right of the cell is sandwiched by the current turn's user's piece'''
    for _col, _row in zip(range(col + 1, max_columns), range(row + 1, max_rows)):
        if board[_col][_row] == NONE:
            return False
        elif board[_col][_row] == turn:
            return True
    return False

# FIN
