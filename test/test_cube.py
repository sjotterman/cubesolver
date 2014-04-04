# testCube.py

import unittest
from ..src import cube

class TestCube(unittest.TestCase):
    def test_blue_start(self):
        myCube = cube.Cube()
        for i in range(0,9):
            self.assertEqual(myCube.face['front'][i], 'b')

    def test_red_start(self):
        myCube = cube.Cube()
        for i in range(0,9):
            self.assertEqual(myCube.face['top'][i], 'r')

    def test_yellow_start(self):
        myCube = cube.Cube()
        for i in range(0,9):
            self.assertEqual(myCube.face['left'][i], 'y')

    def test_orange_start(self):
        myCube = cube.Cube()
        for i in range(0,9):
            self.assertEqual(myCube.face['bottom'][i], 'o')

    def test_white_start(self):
        myCube = cube.Cube()
        for i in range(0,9):
            self.assertEqual(myCube.face['right'][i], 'w')

    def test_green_start(self):
        myCube = cube.Cube()
        for i in range(0,9):
            self.assertEqual(myCube.face['back'][i], 'g')

    def test_start_cube_is_solved(self):
        myCube = cube.Cube()
        self.assertEqual(myCube.is_solved(), True)

    def test_start_then_right_cw(self):
        myCube = cube.Cube()
        myCube.move('right', 'cw')
        
        # right side doesn't change        
        for i in range(0,9):
            self.assertEqual(myCube.face['right'][i], 'w')
        
        # left side doesn't change
        for i in range(0,9):
            self.assertEqual(myCube.face['left'][i], 'y')

        # front side - only three right squares change
        self.assertEqual(myCube.face['front'][0], 'b')
        self.assertEqual(myCube.face['front'][1], 'b')
        self.assertEqual(myCube.face['front'][2], 'o')
        self.assertEqual(myCube.face['front'][3], 'b')
        self.assertEqual(myCube.face['front'][4], 'b')
        self.assertEqual(myCube.face['front'][5], 'o')
        self.assertEqual(myCube.face['front'][6], 'b')
        self.assertEqual(myCube.face['front'][7], 'b')
        self.assertEqual(myCube.face['front'][8], 'o')

        # top side - only three right squares change
        self.assertEqual(myCube.face['top'][0], 'r')
        self.assertEqual(myCube.face['top'][1], 'r')
        self.assertEqual(myCube.face['top'][2], 'b')
        self.assertEqual(myCube.face['top'][3], 'r')
        self.assertEqual(myCube.face['top'][4], 'r')
        self.assertEqual(myCube.face['top'][5], 'b')
        self.assertEqual(myCube.face['top'][6], 'r')
        self.assertEqual(myCube.face['top'][7], 'r')
        self.assertEqual(myCube.face['top'][8], 'b')


        # bottom side - only three right squares change
        self.assertEqual(myCube.face['bottom'][0], 'o')
        self.assertEqual(myCube.face['bottom'][1], 'o')
        self.assertEqual(myCube.face['bottom'][2], 'g')
        self.assertEqual(myCube.face['bottom'][3], 'o')
        self.assertEqual(myCube.face['bottom'][4], 'o')
        self.assertEqual(myCube.face['bottom'][5], 'g')
        self.assertEqual(myCube.face['bottom'][6], 'o')
        self.assertEqual(myCube.face['bottom'][7], 'o')
        self.assertEqual(myCube.face['bottom'][8], 'g')

        # bottom side - only three right squares change
        self.assertEqual(myCube.face['back'][0], 'g')
        self.assertEqual(myCube.face['back'][1], 'g')
        self.assertEqual(myCube.face['back'][2], 'r')
        self.assertEqual(myCube.face['back'][3], 'g')
        self.assertEqual(myCube.face['back'][4], 'g')
        self.assertEqual(myCube.face['back'][5], 'r')
        self.assertEqual(myCube.face['back'][6], 'g')
        self.assertEqual(myCube.face['back'][7], 'g')
        self.assertEqual(myCube.face['back'][8], 'r')

    def test_start_then_right_cw_twice(self):
        myCube = cube.Cube()
        myCube.move('right', 'cw')
        myCube.move('right', 'cw')
        
        # right side doesn't change        
        for i in range(0,9):
            self.assertEqual(myCube.face['right'][i], 'w')
        
        # left side doesn't change
        for i in range(0,9):
            self.assertEqual(myCube.face['left'][i], 'y')

        # front side - only three right squares change
        self.assertEqual(myCube.face['front'][0], 'b')
        self.assertEqual(myCube.face['front'][1], 'b')
        self.assertEqual(myCube.face['front'][2], 'g')
        self.assertEqual(myCube.face['front'][3], 'b')
        self.assertEqual(myCube.face['front'][4], 'b')
        self.assertEqual(myCube.face['front'][5], 'g')
        self.assertEqual(myCube.face['front'][6], 'b')
        self.assertEqual(myCube.face['front'][7], 'b')
        self.assertEqual(myCube.face['front'][8], 'g')

        # top side - only three right squares change
        self.assertEqual(myCube.face['top'][0], 'r')
        self.assertEqual(myCube.face['top'][1], 'r')
        self.assertEqual(myCube.face['top'][2], 'o')
        self.assertEqual(myCube.face['top'][3], 'r')
        self.assertEqual(myCube.face['top'][4], 'r')
        self.assertEqual(myCube.face['top'][5], 'o')
        self.assertEqual(myCube.face['top'][6], 'r')
        self.assertEqual(myCube.face['top'][7], 'r')
        self.assertEqual(myCube.face['top'][8], 'o')


        # bottom side - only three right squares change
        self.assertEqual(myCube.face['bottom'][0], 'o')
        self.assertEqual(myCube.face['bottom'][1], 'o')
        self.assertEqual(myCube.face['bottom'][2], 'r')
        self.assertEqual(myCube.face['bottom'][3], 'o')
        self.assertEqual(myCube.face['bottom'][4], 'o')
        self.assertEqual(myCube.face['bottom'][5], 'r')
        self.assertEqual(myCube.face['bottom'][6], 'o')
        self.assertEqual(myCube.face['bottom'][7], 'o')
        self.assertEqual(myCube.face['bottom'][8], 'r')

        # bottom side - only three right squares change
        self.assertEqual(myCube.face['back'][0], 'g')
        self.assertEqual(myCube.face['back'][1], 'g')
        self.assertEqual(myCube.face['back'][2], 'b')
        self.assertEqual(myCube.face['back'][3], 'g')
        self.assertEqual(myCube.face['back'][4], 'g')
        self.assertEqual(myCube.face['back'][5], 'b')
        self.assertEqual(myCube.face['back'][6], 'g')
        self.assertEqual(myCube.face['back'][7], 'g')
        self.assertEqual(myCube.face['back'][8], 'b')

    def test_start_then_right_cw_4times(self):
        myCube = cube.Cube()
        myCube.move('right', 'cw')
        myCube.move('right', 'cw')
        myCube.move('right', 'cw')
        myCube.move('right', 'cw')

        for i in range(0,9):
            self.assertEqual(myCube.face['front'][i], 'b')
            self.assertEqual(myCube.face['top'][i], 'r')
            self.assertEqual(myCube.face['left'][i], 'y')
            self.assertEqual(myCube.face['bottom'][i], 'o')
            self.assertEqual(myCube.face['right'][i], 'w')
            self.assertEqual(myCube.face['back'][i], 'g')

    def test_start_then_right_ccw(self):
        myCube = cube.Cube()
        myCube.move('right', 'ccw')
        
        # right side doesn't change        
        for i in range(0,9):
            self.assertEqual(myCube.face['right'][i], 'w')
        
        # left side doesn't change
        for i in range(0,9):
            self.assertEqual(myCube.face['left'][i], 'y')

        # front side - only three right squares change
        self.assertEqual(myCube.face['front'][0], 'b')
        self.assertEqual(myCube.face['front'][1], 'b')
        self.assertEqual(myCube.face['front'][2], 'r')
        self.assertEqual(myCube.face['front'][3], 'b')
        self.assertEqual(myCube.face['front'][4], 'b')
        self.assertEqual(myCube.face['front'][5], 'r')
        self.assertEqual(myCube.face['front'][6], 'b')
        self.assertEqual(myCube.face['front'][7], 'b')
        self.assertEqual(myCube.face['front'][8], 'r')

        # top side - only three right squares change
        self.assertEqual(myCube.face['top'][0], 'r')
        self.assertEqual(myCube.face['top'][1], 'r')
        self.assertEqual(myCube.face['top'][2], 'g')
        self.assertEqual(myCube.face['top'][3], 'r')
        self.assertEqual(myCube.face['top'][4], 'r')
        self.assertEqual(myCube.face['top'][5], 'g')
        self.assertEqual(myCube.face['top'][6], 'r')
        self.assertEqual(myCube.face['top'][7], 'r')
        self.assertEqual(myCube.face['top'][8], 'g')


        # bottom side - only three right squares change
        self.assertEqual(myCube.face['bottom'][0], 'o')
        self.assertEqual(myCube.face['bottom'][1], 'o')
        self.assertEqual(myCube.face['bottom'][2], 'b')
        self.assertEqual(myCube.face['bottom'][3], 'o')
        self.assertEqual(myCube.face['bottom'][4], 'o')
        self.assertEqual(myCube.face['bottom'][5], 'b')
        self.assertEqual(myCube.face['bottom'][6], 'o')
        self.assertEqual(myCube.face['bottom'][7], 'o')
        self.assertEqual(myCube.face['bottom'][8], 'b')

        # bottom side - only three right squares change
        self.assertEqual(myCube.face['back'][0], 'g')
        self.assertEqual(myCube.face['back'][1], 'g')
        self.assertEqual(myCube.face['back'][2], 'o')
        self.assertEqual(myCube.face['back'][3], 'g')
        self.assertEqual(myCube.face['back'][4], 'g')
        self.assertEqual(myCube.face['back'][5], 'o')
        self.assertEqual(myCube.face['back'][6], 'g')
        self.assertEqual(myCube.face['back'][7], 'g')
        self.assertEqual(myCube.face['back'][8], 'o')

    def test_start_then_reorient_up(self):
        myCube = cube.Cube()
        myCube.reorient("up")

        for i in range(0,9):
            self.assertEqual(myCube.face['front'][i], 'o')
            self.assertEqual(myCube.face['top'][i], 'b')
            self.assertEqual(myCube.face['left'][i], 'y')
            self.assertEqual(myCube.face['bottom'][i], 'g')
            self.assertEqual(myCube.face['right'][i], 'w')
            self.assertEqual(myCube.face['back'][i], 'r')

    def test_start_then_reorient_down(self):
        myCube = cube.Cube()
        myCube.reorient("down")

        for i in range(0,9):
            self.assertEqual(myCube.face['front'][i], 'r')
            self.assertEqual(myCube.face['top'][i], 'g')
            self.assertEqual(myCube.face['left'][i], 'y')
            self.assertEqual(myCube.face['bottom'][i], 'b')
            self.assertEqual(myCube.face['right'][i], 'w')
            self.assertEqual(myCube.face['back'][i], 'o')

if __name__ == "__main__":
    unittest.main()


