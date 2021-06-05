import config


class Gameboard:
    """
    Gameboard class is used in main file - game.py

It is responsible for:
    - drawing board
    - holding falling tetromino (buffer)
    - holding information about blocks that had fallen earlier
    - detecting which rows should be deleted (and then moving all above one block down)
    """

    def __init__(self):
        """Set proper values of self.fields - 0 when buffer can move and -1 which are borders (undeletable)"""
        # When start all fields are set to 0 (except borders set which are set to -1)
        self.fields = \
            [[config.EMPTY_BLOCK for _ in range(0, config.BOARD_COLUMNS)] for _ in range(0, config.BOARD_ROWS)]

        # set first and last column of i row as border
        for i in range(0, config.BOARD_ROWS - 1):  # except the last row

            self.fields[i][0] = config.BORDER_BLOCK
            self.fields[i][config.BOARD_COLUMNS - 1] = config.BORDER_BLOCK

        for i in range(0, config.BOARD_COLUMNS):
            self.fields[config.BOARD_ROWS - 1][i] = config.BORDER_BLOCK
