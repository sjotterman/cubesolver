# testCube.py

import unittest
from . import cube

class TestCube(unittest.TestCase):
    def test_blue_start(self):
        myCube = cube.Cube()
        for i in range(0,9):
            self.assertEqual(myCube.face['b'][i], 'b')


if __name__ == "__main__":
    unittest.main()


