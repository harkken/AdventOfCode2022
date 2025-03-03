"""
Unit tests for part 2

"""

import unittest

from part2_real import move_head, diagonal_move_adjacent, is_row, is_column, is_adjacent

segments = [[0, 0]] * 10


class TestPart2Methods(unittest.TestCase):
    """
    Test methods in part 2
    """

    def test_move_head(self):
        """
        Test move head
        """
        segments[0] = [1, 1]
        move_head(segments, [1, 0])
        self.assertEqual(segments[0], [2, 1])

    def test_diagonal_move_adjacent(self):
        """
        Test move diagonal
        """
        diagonal_move_adjacent(segments, [4, 1], [2, 2], 1)
        self.assertEqual(segments[1], [3, 2])

    def test_is_row(self):
        """
        In same row
        """
        self.assertEqual(is_row([1, 2], [1, 4]), True)

    def test_is_column(self):
        """
        In same column
        """
        self.assertEqual(is_column([3, 2], [1, 2]), True)

    def test_is_adjacent_should_be_true(self):
        """
        c c c
        c P c
        c c c
        . . .
        """
        adjacent_spots = [
            [1, 1],
            [1, 2],
            [1, 3],
            [2, 1],
            [2, 3],
            [3, 1],
            [3, 2],
            [3, 3],
        ]
        for spot in adjacent_spots:
            self.assertEqual(is_adjacent(spot, [2, 2]), True)

    def test_is_adjacent_should_be_false(self):
        """
        . . .
        x . x
        . . .
        . . .
        """
        self.assertEqual(is_adjacent([2, 1], [2, 3]), False)


if __name__ == "__main__":
    unittest.main()
