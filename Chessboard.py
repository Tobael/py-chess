from typing import Optional
from figures.Figure import Figure
from figures.Pawn import Pawn
from figures.Rook import Rook
from figures.Knight import Knight
from figures.Bishop import Bishop
from figures.Queen import Queen
from figures.King import King
from Colour import Colour


class Chessboard:
    def __init__(self):
        self.board = self._place_figures()

    def get_figure_from_position(self, position: tuple[int, int]) -> Optional[Figure]:
        x, y = position

        return self.board[x][y]

    def _place_figures(self) -> list[list[Optional[Figure]]]:
        return [
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, Pawn(Colour.BLACK), None, None, None, None, None],
            [None, None, Pawn(Colour.WHITE), King(
                Colour.WHITE), None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None]
        ]
