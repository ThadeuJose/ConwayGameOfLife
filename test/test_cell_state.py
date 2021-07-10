from conway import get_cell
import unittest

#Assume cells beyond the boundary are always dead.
class TestCellState(unittest.TestCase):
    def setUp(self):
        self.DEAD_CELL = 0
        self.ALIVE_CELL = 1
        self.start = [[1,0,0],[0,1,1],[1,1,0]]
        self.dead_cell_coord = [(-1, 0), (0, -1), (-1, -1), (0, 3), (3, 0)]

    def test_get_alive_cell(self):
        self.assertEqual(get_cell(self.start, 0, 0), self.ALIVE_CELL)

    def test_get_dead_cell(self):    
        for i, k in self.dead_cell_coord:
            with self.subTest(i=i,k=k):
                self.assertEqual(get_cell(self.start, i, k), self.DEAD_CELL)




