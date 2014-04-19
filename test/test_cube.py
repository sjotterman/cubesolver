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

    def test_start_then_front_up(self):
        myCube = cube.Cube()
        myCube.move('front', 'up')
        
        # right side doesn't change        
        for i in range(0,9):
            self.assertEqual(myCube.face['right'][i], 'w')
        
        # left side doesn't change
        for i in range(0,9):
            self.assertEqual(myCube.face['left'][i], 'y')

        # front side - only three middle squares change
        self.assertEqual(myCube.face['front'][0], 'b')
        self.assertEqual(myCube.face['front'][1], 'o')
        self.assertEqual(myCube.face['front'][2], 'b')
        self.assertEqual(myCube.face['front'][3], 'b')
        self.assertEqual(myCube.face['front'][4], 'o')
        self.assertEqual(myCube.face['front'][5], 'b')
        self.assertEqual(myCube.face['front'][6], 'b')
        self.assertEqual(myCube.face['front'][7], 'o')
        self.assertEqual(myCube.face['front'][8], 'b')

        # top side - only three middle squares change
        self.assertEqual(myCube.face['top'][0], 'r')
        self.assertEqual(myCube.face['top'][1], 'b')
        self.assertEqual(myCube.face['top'][2], 'r')
        self.assertEqual(myCube.face['top'][3], 'r')
        self.assertEqual(myCube.face['top'][4], 'b')
        self.assertEqual(myCube.face['top'][5], 'r')
        self.assertEqual(myCube.face['top'][6], 'r')
        self.assertEqual(myCube.face['top'][7], 'b')
        self.assertEqual(myCube.face['top'][8], 'r')


        # bottom side - only three middle squares change
        self.assertEqual(myCube.face['bottom'][0], 'o')
        self.assertEqual(myCube.face['bottom'][1], 'g')
        self.assertEqual(myCube.face['bottom'][2], 'o')
        self.assertEqual(myCube.face['bottom'][3], 'o')
        self.assertEqual(myCube.face['bottom'][4], 'g')
        self.assertEqual(myCube.face['bottom'][5], 'o')
        self.assertEqual(myCube.face['bottom'][6], 'o')
        self.assertEqual(myCube.face['bottom'][7], 'g')
        self.assertEqual(myCube.face['bottom'][8], 'o')

        # bottom side - only three middle squares change
        self.assertEqual(myCube.face['back'][0], 'g')
        self.assertEqual(myCube.face['back'][1], 'r')
        self.assertEqual(myCube.face['back'][2], 'g')
        self.assertEqual(myCube.face['back'][3], 'g')
        self.assertEqual(myCube.face['back'][4], 'r')
        self.assertEqual(myCube.face['back'][5], 'g')
        self.assertEqual(myCube.face['back'][6], 'g')
        self.assertEqual(myCube.face['back'][7], 'r')
        self.assertEqual(myCube.face['back'][8], 'g')

    def test_start_then_front_rup(self):
        myCube = cube.Cube()
        myCube.move('front', 'rup')
        
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

    def test_start_then_front_lup(self):
        myCube = cube.Cube()
        myCube.move('front', 'lup')
        
        # right side doesn't change        
        for i in range(0,9):
            self.assertEqual(myCube.face['right'][i], 'w')
        
        # left side doesn't change
        for i in range(0,9):
            self.assertEqual(myCube.face['left'][i], 'y')

        # front side - only three left squares change
        self.assertEqual(myCube.face['front'][0], 'o')
        self.assertEqual(myCube.face['front'][1], 'b')
        self.assertEqual(myCube.face['front'][2], 'b')
        self.assertEqual(myCube.face['front'][3], 'o')
        self.assertEqual(myCube.face['front'][4], 'b')
        self.assertEqual(myCube.face['front'][5], 'b')
        self.assertEqual(myCube.face['front'][6], 'o')
        self.assertEqual(myCube.face['front'][7], 'b')
        self.assertEqual(myCube.face['front'][8], 'b')

        # top side - only three left squares change
        self.assertEqual(myCube.face['top'][0], 'b')
        self.assertEqual(myCube.face['top'][1], 'r')
        self.assertEqual(myCube.face['top'][2], 'r')
        self.assertEqual(myCube.face['top'][3], 'b')
        self.assertEqual(myCube.face['top'][4], 'r')
        self.assertEqual(myCube.face['top'][5], 'r')
        self.assertEqual(myCube.face['top'][6], 'b')
        self.assertEqual(myCube.face['top'][7], 'r')
        self.assertEqual(myCube.face['top'][8], 'r')


        # bottom side - only three left squares change
        self.assertEqual(myCube.face['bottom'][0], 'g')
        self.assertEqual(myCube.face['bottom'][1], 'o')
        self.assertEqual(myCube.face['bottom'][2], 'o')
        self.assertEqual(myCube.face['bottom'][3], 'g')
        self.assertEqual(myCube.face['bottom'][4], 'o')
        self.assertEqual(myCube.face['bottom'][5], 'o')
        self.assertEqual(myCube.face['bottom'][6], 'g')
        self.assertEqual(myCube.face['bottom'][7], 'o')
        self.assertEqual(myCube.face['bottom'][8], 'o')

        # bottom side - only three left squares change
        self.assertEqual(myCube.face['back'][0], 'r')
        self.assertEqual(myCube.face['back'][1], 'g')
        self.assertEqual(myCube.face['back'][2], 'g')
        self.assertEqual(myCube.face['back'][3], 'r')
        self.assertEqual(myCube.face['back'][4], 'g')
        self.assertEqual(myCube.face['back'][5], 'g')
        self.assertEqual(myCube.face['back'][6], 'r')
        self.assertEqual(myCube.face['back'][7], 'g')
        self.assertEqual(myCube.face['back'][8], 'g')

    def test_start_then_front_down(self):
        myCube = cube.Cube()
        myCube.move('front', 'down')
        
        # right side doesn't change        
        for i in range(0,9):
            self.assertEqual(myCube.face['right'][i], 'w')
        
        # left side doesn't change
        for i in range(0,9):
            self.assertEqual(myCube.face['left'][i], 'y')

        # front side - only three middle squares change
        self.assertEqual(myCube.face['front'][0], 'b')
        self.assertEqual(myCube.face['front'][1], 'r')
        self.assertEqual(myCube.face['front'][2], 'b')
        self.assertEqual(myCube.face['front'][3], 'b')
        self.assertEqual(myCube.face['front'][4], 'r')
        self.assertEqual(myCube.face['front'][5], 'b')
        self.assertEqual(myCube.face['front'][6], 'b')
        self.assertEqual(myCube.face['front'][7], 'r')
        self.assertEqual(myCube.face['front'][8], 'b')

        # top side - only three middle squares change
        self.assertEqual(myCube.face['top'][0], 'r')
        self.assertEqual(myCube.face['top'][1], 'g')
        self.assertEqual(myCube.face['top'][2], 'r')
        self.assertEqual(myCube.face['top'][3], 'r')
        self.assertEqual(myCube.face['top'][4], 'g')
        self.assertEqual(myCube.face['top'][5], 'r')
        self.assertEqual(myCube.face['top'][6], 'r')
        self.assertEqual(myCube.face['top'][7], 'g')
        self.assertEqual(myCube.face['top'][8], 'r')


        # bottom side - only three middle squares change
        self.assertEqual(myCube.face['bottom'][0], 'o')
        self.assertEqual(myCube.face['bottom'][1], 'b')
        self.assertEqual(myCube.face['bottom'][2], 'o')
        self.assertEqual(myCube.face['bottom'][3], 'o')
        self.assertEqual(myCube.face['bottom'][4], 'b')
        self.assertEqual(myCube.face['bottom'][5], 'o')
        self.assertEqual(myCube.face['bottom'][6], 'o')
        self.assertEqual(myCube.face['bottom'][7], 'b')
        self.assertEqual(myCube.face['bottom'][8], 'o')

        # bottom side - only three middle squares change
        self.assertEqual(myCube.face['back'][0], 'g')
        self.assertEqual(myCube.face['back'][1], 'o')
        self.assertEqual(myCube.face['back'][2], 'g')
        self.assertEqual(myCube.face['back'][3], 'g')
        self.assertEqual(myCube.face['back'][4], 'o')
        self.assertEqual(myCube.face['back'][5], 'g')
        self.assertEqual(myCube.face['back'][6], 'g')
        self.assertEqual(myCube.face['back'][7], 'o')
        self.assertEqual(myCube.face['back'][8], 'g')

    def test_start_then_front_ldown(self):
        myCube = cube.Cube()
        myCube.move('front', 'ldown')
        
        # right side doesn't change        
        for i in range(0,9):
            self.assertEqual(myCube.face['right'][i], 'w')
        
        # left side doesn't change
        for i in range(0,9):
            self.assertEqual(myCube.face['left'][i], 'y')

        # front side - only three left squares change
        self.assertEqual(myCube.face['front'][0], 'r')
        self.assertEqual(myCube.face['front'][1], 'b')
        self.assertEqual(myCube.face['front'][2], 'b')
        self.assertEqual(myCube.face['front'][3], 'r')
        self.assertEqual(myCube.face['front'][4], 'b')
        self.assertEqual(myCube.face['front'][5], 'b')
        self.assertEqual(myCube.face['front'][6], 'r')
        self.assertEqual(myCube.face['front'][7], 'b')
        self.assertEqual(myCube.face['front'][8], 'b')

        # top side - only three left squares change
        self.assertEqual(myCube.face['top'][0], 'g')
        self.assertEqual(myCube.face['top'][1], 'r')
        self.assertEqual(myCube.face['top'][2], 'r')
        self.assertEqual(myCube.face['top'][3], 'g')
        self.assertEqual(myCube.face['top'][4], 'r')
        self.assertEqual(myCube.face['top'][5], 'r')
        self.assertEqual(myCube.face['top'][6], 'g')
        self.assertEqual(myCube.face['top'][7], 'r')
        self.assertEqual(myCube.face['top'][8], 'r')


        # bottom side - only three left squares change
        self.assertEqual(myCube.face['bottom'][0], 'b')
        self.assertEqual(myCube.face['bottom'][1], 'o')
        self.assertEqual(myCube.face['bottom'][2], 'o')
        self.assertEqual(myCube.face['bottom'][3], 'b')
        self.assertEqual(myCube.face['bottom'][4], 'o')
        self.assertEqual(myCube.face['bottom'][5], 'o')
        self.assertEqual(myCube.face['bottom'][6], 'b')
        self.assertEqual(myCube.face['bottom'][7], 'o')
        self.assertEqual(myCube.face['bottom'][8], 'o')

        # bottom side - only three left squares change
        self.assertEqual(myCube.face['back'][0], 'o')
        self.assertEqual(myCube.face['back'][1], 'g')
        self.assertEqual(myCube.face['back'][2], 'g')
        self.assertEqual(myCube.face['back'][3], 'o')
        self.assertEqual(myCube.face['back'][4], 'g')
        self.assertEqual(myCube.face['back'][5], 'g')
        self.assertEqual(myCube.face['back'][6], 'o')
        self.assertEqual(myCube.face['back'][7], 'g')
        self.assertEqual(myCube.face['back'][8], 'g')

    def test_start_then_front_rdown(self):
        myCube = cube.Cube()
        myCube.move('front', 'rdown')
        
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


    def test_start_then_front_right(self):
        myCube = cube.Cube()
        myCube.move('front', 'right')
        
        # top side doesn't change        
        for i in range(0,9):
            self.assertEqual(myCube.face['top'][i], 'r')
        
        # bottom side doesn't change
        for i in range(0,9):
            self.assertEqual(myCube.face['bottom'][i], 'o')

        # front side - only three horizontal middle squares change
        self.assertEqual(myCube.face['front'][0], 'b')
        self.assertEqual(myCube.face['front'][1], 'b')
        self.assertEqual(myCube.face['front'][2], 'b')
        self.assertEqual(myCube.face['front'][3], 'y')
        self.assertEqual(myCube.face['front'][4], 'y')
        self.assertEqual(myCube.face['front'][5], 'y')
        self.assertEqual(myCube.face['front'][6], 'b')
        self.assertEqual(myCube.face['front'][7], 'b')
        self.assertEqual(myCube.face['front'][8], 'b')

        # right side - only three horizontal middle squares change
        self.assertEqual(myCube.face['right'][0], 'w')
        self.assertEqual(myCube.face['right'][1], 'w')
        self.assertEqual(myCube.face['right'][2], 'w')
        self.assertEqual(myCube.face['right'][3], 'b')
        self.assertEqual(myCube.face['right'][4], 'b')
        self.assertEqual(myCube.face['right'][5], 'b')
        self.assertEqual(myCube.face['right'][6], 'w')
        self.assertEqual(myCube.face['right'][7], 'w')
        self.assertEqual(myCube.face['right'][8], 'w')


        # back side - only three horizontal middle squares change
        self.assertEqual(myCube.face['back'][0], 'g')
        self.assertEqual(myCube.face['back'][1], 'g')
        self.assertEqual(myCube.face['back'][2], 'g')
        self.assertEqual(myCube.face['back'][3], 'w')
        self.assertEqual(myCube.face['back'][4], 'w')
        self.assertEqual(myCube.face['back'][5], 'w')
        self.assertEqual(myCube.face['back'][6], 'g')
        self.assertEqual(myCube.face['back'][7], 'g')
        self.assertEqual(myCube.face['back'][8], 'g')

        # left side - only three horizontal middle squares change
        self.assertEqual(myCube.face['left'][0], 'y')
        self.assertEqual(myCube.face['left'][1], 'y')
        self.assertEqual(myCube.face['left'][2], 'y')
        self.assertEqual(myCube.face['left'][3], 'g')
        self.assertEqual(myCube.face['left'][4], 'g')
        self.assertEqual(myCube.face['left'][5], 'g')
        self.assertEqual(myCube.face['left'][6], 'y')
        self.assertEqual(myCube.face['left'][7], 'y')
        self.assertEqual(myCube.face['left'][8], 'y')

    def test_start_then_front_tright(self):
        myCube = cube.Cube()
        myCube.move('front', 'tright')
        
        # top side doesn't change
        for i in range(0,9):
            self.assertEqual(myCube.face['top'][i], 'r')
        
        # bottom side doesn't change
        for i in range(0,9):
            self.assertEqual(myCube.face['bottom'][i], 'o')

        # front side - only three top squares change
        self.assertEqual(myCube.face['front'][0], 'y')
        self.assertEqual(myCube.face['front'][1], 'y')
        self.assertEqual(myCube.face['front'][2], 'y')
        self.assertEqual(myCube.face['front'][3], 'b')
        self.assertEqual(myCube.face['front'][4], 'b')
        self.assertEqual(myCube.face['front'][5], 'b')
        self.assertEqual(myCube.face['front'][6], 'b')
        self.assertEqual(myCube.face['front'][7], 'b')
        self.assertEqual(myCube.face['front'][8], 'b')

        # right side - only three top squares change
        self.assertEqual(myCube.face['right'][0], 'b')
        self.assertEqual(myCube.face['right'][1], 'b')
        self.assertEqual(myCube.face['right'][2], 'b')
        self.assertEqual(myCube.face['right'][3], 'w')
        self.assertEqual(myCube.face['right'][4], 'w')
        self.assertEqual(myCube.face['right'][5], 'w')
        self.assertEqual(myCube.face['right'][6], 'w')
        self.assertEqual(myCube.face['right'][7], 'w')
        self.assertEqual(myCube.face['right'][8], 'w')


        # back side - only three bottom squares change
        self.assertEqual(myCube.face['back'][0], 'g')
        self.assertEqual(myCube.face['back'][1], 'g')
        self.assertEqual(myCube.face['back'][2], 'g')
        self.assertEqual(myCube.face['back'][3], 'g')
        self.assertEqual(myCube.face['back'][4], 'g')
        self.assertEqual(myCube.face['back'][5], 'g')
        self.assertEqual(myCube.face['back'][6], 'w')
        self.assertEqual(myCube.face['back'][7], 'w')
        self.assertEqual(myCube.face['back'][8], 'w')

        # left side - only three top squares change
        self.assertEqual(myCube.face['left'][0], 'g')
        self.assertEqual(myCube.face['left'][1], 'g')
        self.assertEqual(myCube.face['left'][2], 'g')
        self.assertEqual(myCube.face['left'][3], 'y')
        self.assertEqual(myCube.face['left'][4], 'y')
        self.assertEqual(myCube.face['left'][5], 'y')
        self.assertEqual(myCube.face['left'][6], 'y')
        self.assertEqual(myCube.face['left'][7], 'y')
        self.assertEqual(myCube.face['left'][8], 'y')

    def test_start_then_front_bright(self):
        myCube = cube.Cube()
        myCube.move('front', 'bright')
        
        # top side doesn't change
        for i in range(0,9):
            self.assertEqual(myCube.face['top'][i], 'r')
        
        # bottom side doesn't change
        for i in range(0,9):
            self.assertEqual(myCube.face['bottom'][i], 'o')

        # front side - only three bottom squares change
        self.assertEqual(myCube.face['front'][0], 'b')
        self.assertEqual(myCube.face['front'][1], 'b')
        self.assertEqual(myCube.face['front'][2], 'b')
        self.assertEqual(myCube.face['front'][3], 'b')
        self.assertEqual(myCube.face['front'][4], 'b')
        self.assertEqual(myCube.face['front'][5], 'b')
        self.assertEqual(myCube.face['front'][6], 'y')
        self.assertEqual(myCube.face['front'][7], 'y')
        self.assertEqual(myCube.face['front'][8], 'y')

        # right side - only three bottom squares change
        self.assertEqual(myCube.face['right'][0], 'w')
        self.assertEqual(myCube.face['right'][1], 'w')
        self.assertEqual(myCube.face['right'][2], 'w')
        self.assertEqual(myCube.face['right'][3], 'w')
        self.assertEqual(myCube.face['right'][4], 'w')
        self.assertEqual(myCube.face['right'][5], 'w')
        self.assertEqual(myCube.face['right'][6], 'b')
        self.assertEqual(myCube.face['right'][7], 'b')
        self.assertEqual(myCube.face['right'][8], 'b')


        # back side - only three top squares change
        self.assertEqual(myCube.face['back'][0], 'w')
        self.assertEqual(myCube.face['back'][1], 'w')
        self.assertEqual(myCube.face['back'][2], 'w')
        self.assertEqual(myCube.face['back'][3], 'g')
        self.assertEqual(myCube.face['back'][4], 'g')
        self.assertEqual(myCube.face['back'][5], 'g')
        self.assertEqual(myCube.face['back'][6], 'g')
        self.assertEqual(myCube.face['back'][7], 'g')
        self.assertEqual(myCube.face['back'][8], 'g')

        # left side - only three bottom squares change
        self.assertEqual(myCube.face['left'][0], 'y')
        self.assertEqual(myCube.face['left'][1], 'y')
        self.assertEqual(myCube.face['left'][2], 'y')
        self.assertEqual(myCube.face['left'][3], 'y')
        self.assertEqual(myCube.face['left'][4], 'y')
        self.assertEqual(myCube.face['left'][5], 'y')
        self.assertEqual(myCube.face['left'][6], 'g')
        self.assertEqual(myCube.face['left'][7], 'g')
        self.assertEqual(myCube.face['left'][8], 'g')
        
    def test_start_then_reorient_right(self):
        myCube = cube.Cube()
        myCube.reorient("right")

        for i in range(0,9):
            self.assertEqual(myCube.face['front'][i], 'y')
            self.assertEqual(myCube.face['top'][i], 'r')
            self.assertEqual(myCube.face['left'][i], 'g')
            self.assertEqual(myCube.face['bottom'][i], 'o')
            self.assertEqual(myCube.face['right'][i], 'b')
            self.assertEqual(myCube.face['back'][i], 'w')

    def test_start_then_reorient_left(self):
        myCube = cube.Cube()
        myCube.reorient("left")

        for i in range(0,9):
            self.assertEqual(myCube.face['front'][i], 'w')
            self.assertEqual(myCube.face['top'][i], 'r')
            self.assertEqual(myCube.face['left'][i], 'b')
            self.assertEqual(myCube.face['bottom'][i], 'o')
            self.assertEqual(myCube.face['right'][i], 'g')
            self.assertEqual(myCube.face['back'][i], 'y')

    def test_start_front_rup_front_bright(self):
        myCube = cube.Cube()
        myCube.move('front', 'rup')
        myCube.move('front', 'bright')

        self.assertEqual(myCube.face['front'][0], 'b')
        self.assertEqual(myCube.face['front'][1], 'b')
        self.assertEqual(myCube.face['front'][2], 'o')
        self.assertEqual(myCube.face['front'][3], 'b')
        self.assertEqual(myCube.face['front'][4], 'b')
        self.assertEqual(myCube.face['front'][5], 'o')
        self.assertEqual(myCube.face['front'][6], 'y')
        self.assertEqual(myCube.face['front'][7], 'y')
        self.assertEqual(myCube.face['front'][8], 'y')

        self.assertEqual(myCube.face['left'][0], 'y')
        self.assertEqual(myCube.face['left'][1], 'y')
        self.assertEqual(myCube.face['left'][2], 'y')
        self.assertEqual(myCube.face['left'][3], 'y')
        self.assertEqual(myCube.face['left'][4], 'y')
        self.assertEqual(myCube.face['left'][5], 'y')
        self.assertEqual(myCube.face['left'][6], 'r')
        self.assertEqual(myCube.face['left'][7], 'g')
        self.assertEqual(myCube.face['left'][8], 'g')

        self.assertEqual(myCube.face['right'][0], 'w')
        self.assertEqual(myCube.face['right'][1], 'w')
        self.assertEqual(myCube.face['right'][2], 'w')
        self.assertEqual(myCube.face['right'][3], 'w')
        self.assertEqual(myCube.face['right'][4], 'w')
        self.assertEqual(myCube.face['right'][5], 'w')
        self.assertEqual(myCube.face['right'][6], 'b')
        self.assertEqual(myCube.face['right'][7], 'b')
        self.assertEqual(myCube.face['right'][8], 'o')
        
        self.assertEqual(myCube.face['top'][0], 'r')
        self.assertEqual(myCube.face['top'][1], 'r')
        self.assertEqual(myCube.face['top'][2], 'b')
        self.assertEqual(myCube.face['top'][3], 'r')
        self.assertEqual(myCube.face['top'][4], 'r')
        self.assertEqual(myCube.face['top'][5], 'b')
        self.assertEqual(myCube.face['top'][6], 'r')
        self.assertEqual(myCube.face['top'][7], 'r')
        self.assertEqual(myCube.face['top'][8], 'b')

        self.assertEqual(myCube.face['bottom'][0], 'o')
        self.assertEqual(myCube.face['bottom'][1], 'o')
        self.assertEqual(myCube.face['bottom'][2], 'o')
        self.assertEqual(myCube.face['bottom'][3], 'o')
        self.assertEqual(myCube.face['bottom'][4], 'o')
        self.assertEqual(myCube.face['bottom'][5], 'o')
        self.assertEqual(myCube.face['bottom'][6], 'g')
        self.assertEqual(myCube.face['bottom'][7], 'g')
        self.assertEqual(myCube.face['bottom'][8], 'g')
        
        self.assertEqual(myCube.face['back'][0], 'w')
        self.assertEqual(myCube.face['back'][1], 'w')
        self.assertEqual(myCube.face['back'][2], 'w')
        self.assertEqual(myCube.face['back'][3], 'g')
        self.assertEqual(myCube.face['back'][4], 'g')
        self.assertEqual(myCube.face['back'][5], 'r')
        self.assertEqual(myCube.face['back'][6], 'g')
        self.assertEqual(myCube.face['back'][7], 'g')
        self.assertEqual(myCube.face['back'][8], 'r')

    def test_start_front_rup_front_tright(self):
        myCube = cube.Cube()
        myCube.move('front', 'rup')
        myCube.move('front', 'tright')

        self.assertEqual(myCube.face['front'][0], 'y')
        self.assertEqual(myCube.face['front'][1], 'y')
        self.assertEqual(myCube.face['front'][2], 'y')
        self.assertEqual(myCube.face['front'][3], 'b')
        self.assertEqual(myCube.face['front'][4], 'b')
        self.assertEqual(myCube.face['front'][5], 'o')
        self.assertEqual(myCube.face['front'][6], 'b')
        self.assertEqual(myCube.face['front'][7], 'b')
        self.assertEqual(myCube.face['front'][8], 'o')

        self.assertEqual(myCube.face['left'][0], 'r')
        self.assertEqual(myCube.face['left'][1], 'g')
        self.assertEqual(myCube.face['left'][2], 'g')
        self.assertEqual(myCube.face['left'][3], 'y')
        self.assertEqual(myCube.face['left'][4], 'y')
        self.assertEqual(myCube.face['left'][5], 'y')
        self.assertEqual(myCube.face['left'][6], 'y')
        self.assertEqual(myCube.face['left'][7], 'y')
        self.assertEqual(myCube.face['left'][8], 'y')

        self.assertEqual(myCube.face['right'][0], 'b')
        self.assertEqual(myCube.face['right'][1], 'b')
        self.assertEqual(myCube.face['right'][2], 'o')
        self.assertEqual(myCube.face['right'][3], 'w')
        self.assertEqual(myCube.face['right'][4], 'w')
        self.assertEqual(myCube.face['right'][5], 'w')
        self.assertEqual(myCube.face['right'][6], 'w')
        self.assertEqual(myCube.face['right'][7], 'w')
        self.assertEqual(myCube.face['right'][8], 'w')
        
        self.assertEqual(myCube.face['top'][0], 'b')
        self.assertEqual(myCube.face['top'][1], 'b')
        self.assertEqual(myCube.face['top'][2], 'b')
        self.assertEqual(myCube.face['top'][3], 'r')
        self.assertEqual(myCube.face['top'][4], 'r')
        self.assertEqual(myCube.face['top'][5], 'r')
        self.assertEqual(myCube.face['top'][6], 'r')
        self.assertEqual(myCube.face['top'][7], 'r')
        self.assertEqual(myCube.face['top'][8], 'r')

        self.assertEqual(myCube.face['bottom'][0], 'o')
        self.assertEqual(myCube.face['bottom'][1], 'o')
        self.assertEqual(myCube.face['bottom'][2], 'g')
        self.assertEqual(myCube.face['bottom'][3], 'o')
        self.assertEqual(myCube.face['bottom'][4], 'o')
        self.assertEqual(myCube.face['bottom'][5], 'g')
        self.assertEqual(myCube.face['bottom'][6], 'o')
        self.assertEqual(myCube.face['bottom'][7], 'o')
        self.assertEqual(myCube.face['bottom'][8], 'g')
        
        self.assertEqual(myCube.face['back'][0], 'g')
        self.assertEqual(myCube.face['back'][1], 'g')
        self.assertEqual(myCube.face['back'][2], 'r')
        self.assertEqual(myCube.face['back'][3], 'g')
        self.assertEqual(myCube.face['back'][4], 'g')
        self.assertEqual(myCube.face['back'][5], 'r')
        self.assertEqual(myCube.face['back'][6], 'w')
        self.assertEqual(myCube.face['back'][7], 'w')
        self.assertEqual(myCube.face['back'][8], 'w')

    def test_start_then_front_cw(self):
        myCube = cube.Cube()
        myCube.move('front', 'cw')
        
        # back side doesn't change
        for i in range(0,9):
            self.assertEqual(myCube.face['back'][i], 'g')
        
        # front side doesn't change
        for i in range(0,9):
            self.assertEqual(myCube.face['front'][i], 'b')

        # left side - only three right squares change
        self.assertEqual(myCube.face['left'][0], 'y')
        self.assertEqual(myCube.face['left'][1], 'y')
        self.assertEqual(myCube.face['left'][2], 'o')
        self.assertEqual(myCube.face['left'][3], 'y')
        self.assertEqual(myCube.face['left'][4], 'y')
        self.assertEqual(myCube.face['left'][5], 'o')
        self.assertEqual(myCube.face['left'][6], 'y')
        self.assertEqual(myCube.face['left'][7], 'y')
        self.assertEqual(myCube.face['left'][8], 'o')
        
        # right side - only three left squares change
        self.assertEqual(myCube.face['right'][0], 'r')
        self.assertEqual(myCube.face['right'][1], 'w')
        self.assertEqual(myCube.face['right'][2], 'w')
        self.assertEqual(myCube.face['right'][3], 'r')
        self.assertEqual(myCube.face['right'][4], 'w')
        self.assertEqual(myCube.face['right'][5], 'w')
        self.assertEqual(myCube.face['right'][6], 'r')
        self.assertEqual(myCube.face['right'][7], 'w')
        self.assertEqual(myCube.face['right'][8], 'w')
        
        # top side - only three bottom squares change
        self.assertEqual(myCube.face['top'][0], 'r')
        self.assertEqual(myCube.face['top'][1], 'r')
        self.assertEqual(myCube.face['top'][2], 'r')
        self.assertEqual(myCube.face['top'][3], 'r')
        self.assertEqual(myCube.face['top'][4], 'r')
        self.assertEqual(myCube.face['top'][5], 'r')
        self.assertEqual(myCube.face['top'][6], 'y')
        self.assertEqual(myCube.face['top'][7], 'y')
        self.assertEqual(myCube.face['top'][8], 'y')

        # bottom side - only three top squares change
        self.assertEqual(myCube.face['bottom'][0], 'w')
        self.assertEqual(myCube.face['bottom'][1], 'w')
        self.assertEqual(myCube.face['bottom'][2], 'w')
        self.assertEqual(myCube.face['bottom'][3], 'o')
        self.assertEqual(myCube.face['bottom'][4], 'o')
        self.assertEqual(myCube.face['bottom'][5], 'o')
        self.assertEqual(myCube.face['bottom'][6], 'o')
        self.assertEqual(myCube.face['bottom'][7], 'o')
        self.assertEqual(myCube.face['bottom'][8], 'o')
        
    def test_start_front_lup_front_right(self):
        myCube = cube.Cube()
        myCube.move('front', 'lup')
        myCube.move('front', 'right')

        self.assertEqual(myCube.face['front'][0], 'o')
        self.assertEqual(myCube.face['front'][1], 'b')
        self.assertEqual(myCube.face['front'][2], 'b')
        self.assertEqual(myCube.face['front'][3], 'y')
        self.assertEqual(myCube.face['front'][4], 'y')
        self.assertEqual(myCube.face['front'][5], 'y')
        self.assertEqual(myCube.face['front'][6], 'o')
        self.assertEqual(myCube.face['front'][7], 'b')
        self.assertEqual(myCube.face['front'][8], 'b')

        self.assertEqual(myCube.face['left'][0], 'y')
        self.assertEqual(myCube.face['left'][1], 'y')
        self.assertEqual(myCube.face['left'][2], 'y')
        self.assertEqual(myCube.face['left'][3], 'g')
        self.assertEqual(myCube.face['left'][4], 'g')
        self.assertEqual(myCube.face['left'][5], 'r')
        self.assertEqual(myCube.face['left'][6], 'y')
        self.assertEqual(myCube.face['left'][7], 'y')
        self.assertEqual(myCube.face['left'][8], 'y')

        self.assertEqual(myCube.face['right'][0], 'w')
        self.assertEqual(myCube.face['right'][1], 'w')
        self.assertEqual(myCube.face['right'][2], 'w')
        self.assertEqual(myCube.face['right'][3], 'o')
        self.assertEqual(myCube.face['right'][4], 'b')
        self.assertEqual(myCube.face['right'][5], 'b')
        self.assertEqual(myCube.face['right'][6], 'w')
        self.assertEqual(myCube.face['right'][7], 'w')
        self.assertEqual(myCube.face['right'][8], 'w')
        
        self.assertEqual(myCube.face['top'][0], 'b')
        self.assertEqual(myCube.face['top'][1], 'r')
        self.assertEqual(myCube.face['top'][2], 'r')
        self.assertEqual(myCube.face['top'][3], 'b')
        self.assertEqual(myCube.face['top'][4], 'r')
        self.assertEqual(myCube.face['top'][5], 'r')
        self.assertEqual(myCube.face['top'][6], 'b')
        self.assertEqual(myCube.face['top'][7], 'r')
        self.assertEqual(myCube.face['top'][8], 'r')

        self.assertEqual(myCube.face['bottom'][0], 'g')
        self.assertEqual(myCube.face['bottom'][1], 'o')
        self.assertEqual(myCube.face['bottom'][2], 'o')
        self.assertEqual(myCube.face['bottom'][3], 'g')
        self.assertEqual(myCube.face['bottom'][4], 'o')
        self.assertEqual(myCube.face['bottom'][5], 'o')
        self.assertEqual(myCube.face['bottom'][6], 'g')
        self.assertEqual(myCube.face['bottom'][7], 'o')
        self.assertEqual(myCube.face['bottom'][8], 'o')
        
        self.assertEqual(myCube.face['back'][0], 'r')
        self.assertEqual(myCube.face['back'][1], 'g')
        self.assertEqual(myCube.face['back'][2], 'g')
        self.assertEqual(myCube.face['back'][3], 'w')
        self.assertEqual(myCube.face['back'][4], 'w')
        self.assertEqual(myCube.face['back'][5], 'w')
        self.assertEqual(myCube.face['back'][6], 'r')
        self.assertEqual(myCube.face['back'][7], 'g')
        self.assertEqual(myCube.face['back'][8], 'g')

    def test_start_lup_tright_rdown_cw(self):
        myCube = cube.Cube()
        myCube.move('front', 'lup')
        myCube.move('front', 'tright')
        myCube.move('front', 'rdown')
        myCube.move('front', 'cw')

        self.assertEqual(myCube.face['front'][0], 'o')
        self.assertEqual(myCube.face['front'][1], 'o')
        self.assertEqual(myCube.face['front'][2], 'y')
        self.assertEqual(myCube.face['front'][3], 'b')
        self.assertEqual(myCube.face['front'][4], 'b')
        self.assertEqual(myCube.face['front'][5], 'y')
        self.assertEqual(myCube.face['front'][6], 'b')
        self.assertEqual(myCube.face['front'][7], 'r')
        self.assertEqual(myCube.face['front'][8], 'r')

        self.assertEqual(myCube.face['left'][0], 'g')
        self.assertEqual(myCube.face['left'][1], 'g')
        self.assertEqual(myCube.face['left'][2], 'g')
        self.assertEqual(myCube.face['left'][3], 'y')
        self.assertEqual(myCube.face['left'][4], 'y')
        self.assertEqual(myCube.face['left'][5], 'o')
        self.assertEqual(myCube.face['left'][6], 'y')
        self.assertEqual(myCube.face['left'][7], 'y')
        self.assertEqual(myCube.face['left'][8], 'y')

        self.assertEqual(myCube.face['right'][0], 'b')
        self.assertEqual(myCube.face['right'][1], 'w')
        self.assertEqual(myCube.face['right'][2], 'w')
        self.assertEqual(myCube.face['right'][3], 'b')
        self.assertEqual(myCube.face['right'][4], 'w')
        self.assertEqual(myCube.face['right'][5], 'w')
        self.assertEqual(myCube.face['right'][6], 'w')
        self.assertEqual(myCube.face['right'][7], 'w')
        self.assertEqual(myCube.face['right'][8], 'w')
        
        self.assertEqual(myCube.face['top'][0], 'r')
        self.assertEqual(myCube.face['top'][1], 'r')
        self.assertEqual(myCube.face['top'][2], 'g')
        self.assertEqual(myCube.face['top'][3], 'r')
        self.assertEqual(myCube.face['top'][4], 'r')
        self.assertEqual(myCube.face['top'][5], 'g')
        self.assertEqual(myCube.face['top'][6], 'y')
        self.assertEqual(myCube.face['top'][7], 'y')
        self.assertEqual(myCube.face['top'][8], 'r')

        self.assertEqual(myCube.face['bottom'][0], 'o')
        self.assertEqual(myCube.face['bottom'][1], 'b')
        self.assertEqual(myCube.face['bottom'][2], 'b')
        self.assertEqual(myCube.face['bottom'][3], 'g')
        self.assertEqual(myCube.face['bottom'][4], 'o')
        self.assertEqual(myCube.face['bottom'][5], 'b')
        self.assertEqual(myCube.face['bottom'][6], 'g')
        self.assertEqual(myCube.face['bottom'][7], 'o')
        self.assertEqual(myCube.face['bottom'][8], 'b')
        
        self.assertEqual(myCube.face['back'][0], 'r')
        self.assertEqual(myCube.face['back'][1], 'g')
        self.assertEqual(myCube.face['back'][2], 'o')
        self.assertEqual(myCube.face['back'][3], 'r')
        self.assertEqual(myCube.face['back'][4], 'g')
        self.assertEqual(myCube.face['back'][5], 'o')
        self.assertEqual(myCube.face['back'][6], 'w')
        self.assertEqual(myCube.face['back'][7], 'w')
        self.assertEqual(myCube.face['back'][8], 'o')
        
    def test_start_solved_status(self):
        myCube = cube.Cube()
        self.assertEqual(myCube.solved_status(), 100)
    
    def test_start_rup_solved_status(self):
        myCube = cube.Cube()
        myCube.move('front', 'rup')
        self.assertTrue(myCube.solved_status() < 78,
            "Status = " + str(myCube.solved_status()))
        self.assertTrue(myCube.solved_status() > 77,
            "Status = " + str(myCube.solved_status()))

    def test_start_reorient_cw(self):
        myCube = cube.Cube()
        myCube.reorient('cw')
        for i in range(0,9):
            self.assertEqual(myCube.face['front'][i], 'b')
            self.assertEqual(myCube.face['top'][i], 'y')
            self.assertEqual(myCube.face['left'][i], 'o')
            self.assertEqual(myCube.face['bottom'][i], 'w')
            self.assertEqual(myCube.face['right'][i], 'r')
            self.assertEqual(myCube.face['back'][i], 'g')

    def test_start_reorient_ccw(self):
        myCube = cube.Cube()
        myCube.reorient('ccw')
        for i in range(0,9):
            self.assertEqual(myCube.face['front'][i], 'b')
            self.assertEqual(myCube.face['top'][i], 'w')
            self.assertEqual(myCube.face['left'][i], 'r')
            self.assertEqual(myCube.face['bottom'][i], 'y')
            self.assertEqual(myCube.face['right'][i], 'o')
            self.assertEqual(myCube.face['back'][i], 'g')


    def test_start_tright_frontdown_front_left(self):
        myCube = cube.Cube()
        myCube.move('front','tright')
        myCube.move('front','down')
        myCube.move('front','left')


        self.assertEqual(myCube.face['front'][0], 'y')
        self.assertEqual(myCube.face['front'][1], 'r')
        self.assertEqual(myCube.face['front'][2], 'y')
        self.assertEqual(myCube.face['front'][3], 'w')
        self.assertEqual(myCube.face['front'][4], 'w')
        self.assertEqual(myCube.face['front'][5], 'w')
        self.assertEqual(myCube.face['front'][6], 'b')
        self.assertEqual(myCube.face['front'][7], 'r')
        self.assertEqual(myCube.face['front'][8], 'b')

        self.assertEqual(myCube.face['left'][0], 'g')
        self.assertEqual(myCube.face['left'][1], 'g')
        self.assertEqual(myCube.face['left'][2], 'g')
        self.assertEqual(myCube.face['left'][3], 'b')
        self.assertEqual(myCube.face['left'][4], 'r')
        self.assertEqual(myCube.face['left'][5], 'b')
        self.assertEqual(myCube.face['left'][6], 'y')
        self.assertEqual(myCube.face['left'][7], 'y')
        self.assertEqual(myCube.face['left'][8], 'y')

        self.assertEqual(myCube.face['right'][0], 'b')
        self.assertEqual(myCube.face['right'][1], 'b')
        self.assertEqual(myCube.face['right'][2], 'b')
        self.assertEqual(myCube.face['right'][3], 'g')
        self.assertEqual(myCube.face['right'][4], 'o')
        self.assertEqual(myCube.face['right'][5], 'g')
        self.assertEqual(myCube.face['right'][6], 'w')
        self.assertEqual(myCube.face['right'][7], 'w')
        self.assertEqual(myCube.face['right'][8], 'w')
        
        self.assertEqual(myCube.face['top'][0], 'r')
        self.assertEqual(myCube.face['top'][1], 'g')
        self.assertEqual(myCube.face['top'][2], 'r')
        self.assertEqual(myCube.face['top'][3], 'r')
        self.assertEqual(myCube.face['top'][4], 'g')
        self.assertEqual(myCube.face['top'][5], 'r')
        self.assertEqual(myCube.face['top'][6], 'r')
        self.assertEqual(myCube.face['top'][7], 'w')
        self.assertEqual(myCube.face['top'][8], 'r')

        self.assertEqual(myCube.face['bottom'][0], 'o')
        self.assertEqual(myCube.face['bottom'][1], 'y')
        self.assertEqual(myCube.face['bottom'][2], 'o')
        self.assertEqual(myCube.face['bottom'][3], 'o')
        self.assertEqual(myCube.face['bottom'][4], 'b')
        self.assertEqual(myCube.face['bottom'][5], 'o')
        self.assertEqual(myCube.face['bottom'][6], 'o')
        self.assertEqual(myCube.face['bottom'][7], 'b')
        self.assertEqual(myCube.face['bottom'][8], 'o')
        
        self.assertEqual(myCube.face['back'][0], 'g')
        self.assertEqual(myCube.face['back'][1], 'o')
        self.assertEqual(myCube.face['back'][2], 'g')
        self.assertEqual(myCube.face['back'][3], 'y')
        self.assertEqual(myCube.face['back'][4], 'y')
        self.assertEqual(myCube.face['back'][5], 'y')
        self.assertEqual(myCube.face['back'][6], 'w')
        self.assertEqual(myCube.face['back'][7], 'o')
        self.assertEqual(myCube.face['back'][8], 'w')

    def test_start_reorient_up_blue_face_solved(self):
        myCube = cube.Cube()
        myCube.reorient('up')
        self.assertEqual(myCube.isFirstLayerSolved('b'), True)
    
    def test_start_blue_face_solved(self):
        myCube = cube.Cube()
        self.assertEqual(myCube.isFirstLayerSolved('b'), True)
    
    def test_start_blue_middle_layer_solved(self):
        myCube = cube.Cube()
        self.assertEqual(myCube.isSecondLayerSolved('b'), True)
    
    def test_start_reorient_up_blue_middle_layer_solved(self):
        myCube = cube.Cube()
        myCube.reorient('up')
        self.assertEqual(myCube.isSecondLayerSolved('b'), True)

    def test_start_reorient_up_rup_blue_middle_layer_solved(self):
        myCube = cube.Cube()
        myCube.reorient('up')
        myCube.move('front','rup')
        self.assertEqual(myCube.isSecondLayerSolved('b'), False)
    
    def test_start_blue_rup_middle_layer_solved(self):
        myCube = cube.Cube()
        myCube.move('front','rup')
        self.assertEqual(myCube.isSecondLayerSolved('b'), False)

    def test_start_rotate_second_layer_solved(self):
        myCube = cube.Cube()
        myCube.reorient("left")
        myCube.move("front", "up")
        myCube.reorient("right")
        self.assertEqual(myCube.isSecondLayerSolved('b'), True)

    def test_start_rotate_second_layer_y_solved(self):
        myCube = cube.Cube()
        myCube.move("front", "up")
        self.assertEqual(myCube.isSecondLayerSolved('y'), True)

    def test_start_front_rup_blue_face_solved(self):
        myCube = cube.Cube()
        myCube.move('front', 'rup')
        self.assertEqual(myCube.isFirstLayerSolved('b'), False)

    def test_switch_blue_cubes_face_solved(self):
        myCube = cube.Cube()

        myCube.reorient('up')
        myCube.move('front','down')
        myCube.move('front','bright')
        myCube.move('front','up')
        myCube.reorient('left')
        myCube.move('front','ccw')
        myCube.move('front','left')
        myCube.move('front','cw')
        myCube.reorient('right')
        myCube.move('front', 'left')
        myCube.move('front','ccw')
        myCube.move('middle', 'right')
        myCube.move('front', 'cw')
        self.assertEqual(myCube.isFirstLayerSolved('b'), False)

    def test_reorientup_down_bright(self):
        myCube = cube.Cube()
        myCube.reorient('up')
        myCube.move('front','down')
        myCube.move('front','bright')

        self.assertEqual(myCube.face['front'][0], 'o')
        self.assertEqual(myCube.face['front'][1], 'b')
        self.assertEqual(myCube.face['front'][2], 'o')
        self.assertEqual(myCube.face['front'][3], 'o')
        self.assertEqual(myCube.face['front'][4], 'b')
        self.assertEqual(myCube.face['front'][5], 'o')
        self.assertEqual(myCube.face['front'][6], 'y')
        self.assertEqual(myCube.face['front'][7], 'y')
        self.assertEqual(myCube.face['front'][8], 'y')

        self.assertEqual(myCube.face['left'][0], 'y')
        self.assertEqual(myCube.face['left'][1], 'y')
        self.assertEqual(myCube.face['left'][2], 'y')
        self.assertEqual(myCube.face['left'][3], 'y')
        self.assertEqual(myCube.face['left'][4], 'y')
        self.assertEqual(myCube.face['left'][5], 'y')
        self.assertEqual(myCube.face['left'][6], 'r')
        self.assertEqual(myCube.face['left'][7], 'g')
        self.assertEqual(myCube.face['left'][8], 'r')

        self.assertEqual(myCube.face['right'][0], 'w')
        self.assertEqual(myCube.face['right'][1], 'w')
        self.assertEqual(myCube.face['right'][2], 'w')
        self.assertEqual(myCube.face['right'][3], 'w')
        self.assertEqual(myCube.face['right'][4], 'w')
        self.assertEqual(myCube.face['right'][5], 'w')
        self.assertEqual(myCube.face['right'][6], 'o')
        self.assertEqual(myCube.face['right'][7], 'b')
        self.assertEqual(myCube.face['right'][8], 'o')
        
        self.assertEqual(myCube.face['top'][0], 'b')
        self.assertEqual(myCube.face['top'][1], 'r')
        self.assertEqual(myCube.face['top'][2], 'b')
        self.assertEqual(myCube.face['top'][3], 'b')
        self.assertEqual(myCube.face['top'][4], 'r')
        self.assertEqual(myCube.face['top'][5], 'b')
        self.assertEqual(myCube.face['top'][6], 'b')
        self.assertEqual(myCube.face['top'][7], 'r')
        self.assertEqual(myCube.face['top'][8], 'b')

        self.assertEqual(myCube.face['bottom'][0], 'g')
        self.assertEqual(myCube.face['bottom'][1], 'g')
        self.assertEqual(myCube.face['bottom'][2], 'g')
        self.assertEqual(myCube.face['bottom'][3], 'o')
        self.assertEqual(myCube.face['bottom'][4], 'o')
        self.assertEqual(myCube.face['bottom'][5], 'o')
        self.assertEqual(myCube.face['bottom'][6], 'g')
        self.assertEqual(myCube.face['bottom'][7], 'g')
        self.assertEqual(myCube.face['bottom'][8], 'g')
        
        self.assertEqual(myCube.face['back'][0], 'w')
        self.assertEqual(myCube.face['back'][1], 'w')
        self.assertEqual(myCube.face['back'][2], 'w')
        self.assertEqual(myCube.face['back'][3], 'r')
        self.assertEqual(myCube.face['back'][4], 'g')
        self.assertEqual(myCube.face['back'][5], 'r')
        self.assertEqual(myCube.face['back'][6], 'r')
        self.assertEqual(myCube.face['back'][7], 'g')
        self.assertEqual(myCube.face['back'][8], 'r')


if __name__ == "__main__":
    unittest.main()


