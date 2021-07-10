from conway import next_gen, sum_neighbours_cells
import unittest

class TestConwayGameMethods(unittest.TestCase):

    def test_if_work(self):
        glider =  [[1,0,0,0,0,0,0],
           [0,1,1,0,0,0,0],
           [1,1,0,0,0,0,0],
           [0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0]]
        glider_solution = [[0,1,0,0,0,0,0],
                           [0,0,1,0,0,0,0],
                           [1,1,1,0,0,0,0],
                           [0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0]]

        self.assertEqual(next_gen(glider), glider_solution)

    def test_sum_neighbours_cells(self):
        start = [[1,0,0],
                [0,1,1],
                [1,1,0]]
        cell_x = 1
        cell_y = 1
        
        sum = sum_neighbours_cells(start, cell_x, cell_y)

        output_sum = 4

        self.assertEqual(sum, output_sum)
 
