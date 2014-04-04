# testCube.py

import unittest
from . import cube

class TestCube(unittest.TestCase):
    def test_blue_start(self):
        myCube = cube.Cube()
        for i in range(0,9):
            self.assertEqual(myCube.face['b'][i], 'b')

    def test_red_start(self):
        myCube = cube.Cube()
        for i in range(0,9):
            self.assertEqual(myCube.face['r'][i], 'r')

    def test_yellow_start(self):
        myCube = cube.Cube()
        for i in range(0,9):
            self.assertEqual(myCube.face['y'][i], 'y')

    def test_orange_start(self):
        myCube = cube.Cube()
        for i in range(0,9):
            self.assertEqual(myCube.face['o'][i], 'o')

    def test_white_start(self):
        myCube = cube.Cube()
        for i in range(0,9):
            self.assertEqual(myCube.face['w'][i], 'w')

    def test_green_start(self):
        myCube = cube.Cube()
        for i in range(0,9):
            self.assertEqual(myCube.face['g'][i], 'g')

if __name__ == "__main__":
    unittest.main()


