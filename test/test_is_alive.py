from conway import is_alive
import unittest

class TestIsAliveMethods(unittest.TestCase):
    '''
    Case    C   N                 new C
    1       1   0,1             ->  0  # Lonely
    2       1   4,5,6,7,8       ->  0  # Overcrowded
    3       1   2,3             ->  1  # Lives
    4       0   3               ->  1  # It takes three to give birth!
    5       0   0,1,2,4,5,6,7,8 ->  0  # Barren
    '''

    def test_is_alive(self):    
        cases = [(1, 0, False),(1, 1, False),(1, 2, True),(1, 3, True), (1, 4, False),
        (0, 0, False),(0, 1, False),(0, 2, False),(0, 3, True), (0, 4, False)]    
        for cell, sum, value in cases:
            with self.subTest(cell=cell,sum=sum):
                self.assertIs(is_alive(cell,sum),value)
