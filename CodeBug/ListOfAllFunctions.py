import codebug_tether
import codebug_tether.sprites

    def _int_input_index(self, input_index):
        """Returns an integer input index."""
        # 'A' is 4, 'B' is 5

    def get_input(self, input_index):
        """Returns the state of an input. You can use 'A' and 'B' to
        access buttons A and B.

            >>> with CodeBug() as codebug:
            ...     codebug.get_input('A')  # switch A is unpressed
            ...
            0
            >>> codebug.get_input(0)  # assuming pad 0 is connected to GND
            1

        """

    def set_output(self, output_index, state):
        """Sets the output at index to state. `1` or `True` is ON, `0` or
        `False` is OFF.
        """

    def set_leg_io(self, leg_index, direction):
        """Sets the I/O direction of the leg at index. 1 is Input, 0 is Output.
        """

    def clear(self):
        """Clears the LED's on CodeBug.

            >>> with CodeBug() as codebug:
            ...     codebug.clear()
            ...

        """

    def set_row(self, row, val):
        """Sets a row of LEDs on CodeBug.

            >>> with CodeBug() as codebug:
            ...     codebug.set_row(0, 0b10101)
            ...

        """

    def get_row(self, row):
        """Returns a row of LEDs on CodeBug.

            >>> with CodeBug() as codebug:
            ...     codebug.get_row(0)
            ...
            21

        """

    def set_col(self, col, val):
        """Sets an entire column of LEDs on CodeBug.

            >>> with CodeBug() as codebug:
            ...     codebug.set_col(0, 0b10101)
            ...

        """

    def get_col(self, col):
        """Returns an entire column of LEDs on CodeBug.

            >>> with CodeBug() as codebug:
            ...     codebug.get_col(0)
            ...
            21

        """

    def set_pixel(self, x, y, state):
        """Sets a pixel on CodeBug.

            >>> with CodeBug() as codebug:
            ...     codebug.set_pixel(0, 0, 1)
            ...

        """

    def get_pixel(self, x, y):
        """Returns the state of an LED on CodeBug.

            >>> with CodeBug() as codebug:
            ...     codebug.get_pixel(0, 0)
            ...
            1

        """

    def write_text(self, x, y, message, direction="right"):
        """Writes some text on CodeBug at LED (x, y).

            >>> with CodeBug() as codebug:
            ...     codebug.write_text(0, 0, 'Hello, CodeBug!')
            ...

        """

    """-------------SPRITES------------""" 
    >>> # create a 3x3 square with the middle pixel off
    >>> square_sprite = codebug_tether.sprites.Sprite(3, 3)
    >>> square_sprite.set_row(0, 0b111)
    >>> square_sprite.set_row(1, 0b101)
    >>> square_sprite.set_row(2, 0b111)

    >>> # draw it in the middle of CodeBug
    >>> codebug = codebug_tether.CodeBug()
    >>> codebug.draw_sprite(1, 1, square_sprite)

    >>> # write some text
    >>> message = codebug_tether.sprites.StringSprite('Hello CodeBug!')
    >>> codebug.draw_sprite(0, 0, message)
    >>> # move it along
    >>> codebug_i2c_tetherbug.draw_sprite(-2, 0, message)


