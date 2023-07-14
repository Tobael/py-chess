from typing import Optional, TYPE_CHECKING

from Colour import Colour
from figures.Figure import Figure
from figures.Rook import Rook

if TYPE_CHECKING:
    from Chessboard import Chessboard


class King(Figure):

    def __init__(self, colour: Colour):
        super().__init__(colour)
        self.has_moved = False

    def get_picture(self):
        return "♔" if self.colour == Colour.WHITE else "♚"

    def get_moves(self, position: tuple[int, int], chessboard: "Chessboard") -> list[tuple[int, int]]:
        moves = []
        x, y = position

        if x + 1 < 8 and (
                chessboard.get_figure_from_position((x + 1, y)) is None or chessboard.get_figure_from_position(
            (x + 1, y)).colour != self.colour):
            moves.append((x + 1, y))
        if x + 1 < 8 and y + 1 < 8 and (
                chessboard.get_figure_from_position((x + 1, y + 1)) is None or chessboard.get_figure_from_position(
            (x + 1, y + 1)).colour != self.colour):
            moves.append((x + 1, y + 1))
        if x + 1 < 8 and y - 1 >= 0 and (
                chessboard.get_figure_from_position((x + 1, y - 1)) is None or chessboard.get_figure_from_position(
            (x + 1, y - 1)).colour != self.colour):
            moves.append((x + 1, y - 1))
        if y + 1 < 8 and (
                chessboard.get_figure_from_position((x, y + 1)) is None or chessboard.get_figure_from_position(
            (x, y + 1)).colour != self.colour):
            moves.append((x, y + 1))
        if y - 1 < 8 and (
                chessboard.get_figure_from_position((x, y - 1)) is None or chessboard.get_figure_from_position(
            (x, y - 1)).colour != self.colour):
            moves.append((x, y - 1))
        if x - 1 >= 0 and (
                chessboard.get_figure_from_position((x - 1, y)) is None or chessboard.get_figure_from_position(
            (x - 1, y)).colour != self.colour):
            moves.append((x - 1, y))
        if x - 1 >= 0 and y + 1 < 8 and (
                chessboard.get_figure_from_position((x - 1, y + 1)) is None or chessboard.get_figure_from_position(
            (x - 1, y + 1)).colour != self.colour):
            moves.append((x - 1, y + 1))
        if x - 1 >= 0 and y - 1 >= 0 and (
                chessboard.get_figure_from_position((x - 1, y - 1)) is None or chessboard.get_figure_from_position(
            (x - 1, y - 1)).colour != self.colour):
            moves.append((x - 1, y - 1))

        # Castling
        if not self.has_moved:
            left_rook = chessboard.get_figure_from_position((x, 0))
            right_rook = chessboard.get_figure_from_position((x, 7))
            if isinstance(left_rook, Rook) and not left_rook.has_moved:
                moves.append((x, 1))
            if isinstance(right_rook, Rook) and not right_rook.has_moved:
                moves.append((x, 5))

        return moves
