# othello_gui.py ICS 32 Lab. Elton Xue 52611936

##################
# Import Modules #
##################

import othello_point
import othello_logic
import tkinter

#########
# Fonts #
#########

DEFAULT_FONT = ('Helvetica', 12)

###########
# Classes #
###########

class OthelloInputs:
    def __init__(self):
        ''' Creates the entire game options window'''
        self._menu_window = tkinter.Tk()

        title = tkinter.Label(master = self._menu_window, text = 'OTHELLO GAME OPTIONS', font = ('Helvetica', 15, 'bold'))

        title.grid(row = 0, column = 0, columnspan = 2)

        self._rows_and_columns()
        self._first_turn_and_start_arrangement()
        self._winning_rules()

        button_frame = tkinter.Frame(master = self._menu_window)
        
        button_frame.grid(
            row = 6, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.E + tkinter.S)

        ok_button = tkinter.Button(
            master = button_frame, text = 'OK', font = DEFAULT_FONT, 
            command = self._on_ok_button)

        ok_button.grid(row = 0, column = 0, padx = 10, pady = 10)

        self._menu_window.rowconfigure(6, weight = 1)
        self._menu_window.columnconfigure(1, weight = 1)

        self._menu_window.mainloop()

    def get_rows(self) -> int:
        '''Returns the number of rows the user chooses'''
        return self._rows

    def get_columns(self) -> int:
        '''Returns the number of columns the user chooses'''
        return self._columns

    def get_first_turn(self) -> str:
        '''Returns the first turn the user chooses'''
        return self._first_turn

    def get_start_arrangement(self) -> str:
        '''Returns the start arrangement the user chooses'''
        return self._start_arrangement

    def get_winning_rules(self) -> str:
        '''Returns the winning rules the user chooses'''
        return self._winning_rules

    def _on_ok_button(self) -> None:
        '''Assigns new variables to all the variables that are in each option and destroys the menu window'''
        self._rows = self._row_variable.get()
        self._columns = self._col_variable.get()
        self._first_turn = self._first_turn_variable.get()
        self._start_arrangement = self._start_arrangement_variable.get()
        self._winning_rules = self._winning_rules_variable.get()

        self._menu_window.destroy()

    def _rows_and_columns(self) -> None:
        '''Creates the rows and columns options'''
        rows_label = tkinter.Label(
            master = self._menu_window, text = 'Rows:',
            font = DEFAULT_FONT)

        rows_label.grid(
            row = 1, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._row_variable = tkinter.IntVar()
        self._row_variable.set(4)
        self._rows_menu = tkinter.OptionMenu(self._menu_window, self._row_variable, 4, 6, 8, 10, 12, 14, 16)
        
        self._rows_menu.grid(
            row = 1, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E) 
                
        columns_label = tkinter.Label(
            master = self._menu_window, text = 'Columns:',
            font = DEFAULT_FONT)

        columns_label.grid(
            row = 2, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._col_variable = tkinter.IntVar()
        self._col_variable.set(4)
        self._columns_menu = tkinter.OptionMenu(self._menu_window, self._col_variable, 4, 6, 8, 10, 12, 14, 16)

        self._columns_menu.grid(
            row = 2, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)


    def _first_turn_and_start_arrangement(self) -> None:
        '''Creates the first turn and start arrangement options'''
        first_turn_label = tkinter.Label(
            master = self._menu_window, text = 'First turn (Black or White):',
            font = DEFAULT_FONT)

        first_turn_label.grid(
            row = 3, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._first_turn_variable = tkinter.StringVar()
        self._first_turn_variable.set('B')
        self._first_turn_menu = tkinter.OptionMenu(self._menu_window, self._first_turn_variable, 'B','W')
        
        self._first_turn_menu.grid(
            row = 3, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E) 
                
        start_arrangement_label = tkinter.Label(
            master = self._menu_window, text = 'Start Arrangement (Black or White):',
            font = DEFAULT_FONT)

        start_arrangement_label.grid(
            row = 4, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._start_arrangement_variable = tkinter.StringVar()
        self._start_arrangement_variable.set('B')
        self._start_arrangement_menu = tkinter.OptionMenu(self._menu_window, self._start_arrangement_variable, 'B', 'W')

        self._start_arrangement_menu.grid(
            row = 4, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)

    def _winning_rules(self):
        '''Creates the winning rules option'''
        winning_rules_label = tkinter.Label(
            master = self._menu_window, text = 'Winning Rules (Greater Than or Less Than):',
            font = DEFAULT_FONT)
        
        winning_rules_label.grid(
            row = 5, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._winning_rules_variable = tkinter.StringVar()
        self._winning_rules_variable.set('>')
        self._winning_rules_menu = tkinter.OptionMenu(self._menu_window, self._winning_rules_variable, '>', '<')
        
        self._winning_rules_menu.grid(
            row = 5, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E) 

class OthelloGUI:
    def __init__(self):
        '''Initializes the GUI by taking in the inputs the user chooses
        and then creates the entire Othello game window'''

        self._OthelloInputs = OthelloInputs()

        self._rows = self._OthelloInputs.get_rows()
        self._columns = self._OthelloInputs.get_columns()
        self._first_turn = self._OthelloInputs.get_first_turn()
        self._start_arrangement = self._OthelloInputs.get_start_arrangement()
        self._winning_rules = self._OthelloInputs.get_winning_rules()
        
        self._OthelloState = othello_logic.GameState(self._rows, self._columns, self._start_arrangement, self._first_turn)
        
        self._board = self._OthelloState.board()
    
        self._root_window = tkinter.Tk()

        self._game_status = tkinter.StringVar()

        self._status = tkinter.Label(
            master = self._root_window,
            width = 30, height = 3, textvariable = self._game_status, font = DEFAULT_FONT)

        self._status.grid(row = 0, column = 0)

        self._canvas = tkinter.Canvas(
            master = self._root_window,
            width = self._columns * 50, height = self._rows * 50,
            background = 'darkgreen')

        self._canvas.grid(
            row = 1, column = 0,
            sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)

        self._canvas.bind('<Configure>', self._on_canvas_resized)
        self._canvas.bind('<Button-1>', self._on_canvas_clicked)

        self._root_window.rowconfigure(1, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)

    def start(self) -> None:
        '''Starts the Othello game'''
        self._root_window.mainloop()

    def _on_canvas_resized(self, event: tkinter.Event) -> None:
        '''Handles the situation in which the game window is resized.
        Redraws the game board and updates the game status'''
        self._redraw_game_board()
        self._update_game_status()

    def _on_canvas_clicked(self, event: tkinter.Event) -> None:
        '''Handles the situation in which a cell is clicked and then checks if
        such row and column is a valid move. If not, it does nothing. If
        it is, it makes the move'''
        click_point = (event.x, event.y)
        row_and_column = self._handle_click(click_point)
        
        try:
            row, col = row_and_column
            self._make_move(row, col)
        except:
            return
        
        
    def _redraw_game_board(self) -> None:
        '''Redraws the entire gameboard through the use of iteration and rectangles. Also
        takes into account the top left and bottom right corners of each rectangle in a list of tuples
        for other uses, such as depicting which row and column the user clicks'''

        self._canvas.delete(tkinter.ALL)
        
        self._list_cells = []

        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()

        corner_point = othello_point.from_pixel(0, 0, canvas_width, canvas_height)
        corner_cell = corner_point.frac()
        corner_x, corner_y = corner_cell

        cell_width = canvas_width/self._columns
        cell_height = canvas_height/self._rows

        for row in range(self._rows):
            for col in range(self._columns):
                
                self._canvas.create_rectangle(corner_x, corner_y, corner_x + cell_width, corner_y + cell_height, outline = 'black')

                frac_top = othello_point.from_pixel(corner_x, corner_y, canvas_width, canvas_height)
                frac_bottom = othello_point.from_pixel(corner_x + cell_width, corner_y + cell_height, canvas_width, canvas_height)

                self._list_cells.append(((frac_top.frac()), (frac_bottom.frac())))
                
                corner_x += cell_width
                
                if self._board[col][row] == othello_logic.BLACK:
                    self._canvas.create_oval(corner_x - cell_width + 2, corner_y + 2, corner_x - 2,  corner_y + cell_height - 2, fill = 'black')
                elif self._board[col][row] == othello_logic.WHITE:
                    self._canvas.create_oval(corner_x - cell_width + 2, corner_y + 2, corner_x - 2, corner_y + cell_height - 2, fill = 'white')
                    
            corner_x = 0
            corner_y += cell_height
            
    def _update_game_status(self) -> None:
        '''Displays the current game status. If the game is over,
        it displays the winner of the game instead of the turn'''
        self._game_status.set('BLACK:  {}   WHITE:  {}\nTURN:  {}   RULES: FULL'.format(othello_logic.check_black_pieces(self._board),
                                                                   othello_logic.check_white_pieces(self._board),
                                                                   self._get_turn()))
        if not self._OthelloState.game_over():
            self._game_status.set('-----GAME OVER-----\nBLACK:  {}   WHITE:  {}\nWINNER:  {}   RULES: FULL'.format(othello_logic.check_black_pieces(self._board),
                                                                   othello_logic.check_white_pieces(self._board),
                                                                   self._get_winner()))
            
    def _get_turn(self) -> str:
        '''Returns the turn in a string type for display purposes'''
        if self._OthelloState.turn() == othello_logic.BLACK:
            return 'BLACK'
        else:
            return 'WHITE'
            
    def _get_winner(self) -> str:
        '''Returns the winner in a string type for display purposes'''
        winner = self._OthelloState.winner(self._winning_rules)
        if winner == othello_logic.BLACK:
            return 'BLACK'
        elif winner == othello_logic.WHITE:
            return 'WHITE'
        else:
            return 'NONE'
        
    def _make_move(self, row: int, col: int) -> None:
        '''Checks if the move is valid, if there is a need to skip a turn,
        and if the game is over'''
        if self._OthelloState.make_move(row, col):
            self._redraw_game_board()
        if self._OthelloState.game_over():
            self._update_game_status()
        self._update_game_status()

    def _handle_click(self, point: othello_point.Point) -> tuple:
        '''Handles where the user clicks inside the game window. Takes
        where they clicked and converts its pixels into fractional form. Then
        checks which row and column that click is in. Returns that row and column in a tuple'''

        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()
        
        click_x, click_y = point
        click_point = othello_point.from_pixel(click_x, click_y, canvas_width, canvas_height)
        frac_x, frac_y = click_point.frac()

        row_num = 1
        col_num = 1

        for cell_corners in self._list_cells:
            
            top_left_corner, bottom_right_corner = cell_corners
            top_x, top_y = top_left_corner
            bottom_x, bottom_y = bottom_right_corner
            
            if frac_x > top_x and frac_x < bottom_x and frac_y > top_y and frac_y < bottom_y:
                row = row_num
                col = col_num
                return (row, col)
            if col_num == self._columns:
                col_num = 0
                row_num += 1
                
            col_num += 1
            
###########
# Run GUI #
###########

if __name__ == '__main__':
    try:
        OthelloGUI().start()
    except:
        pass


