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

if __name__ == "__main__":
    unittest.main()


