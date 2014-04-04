# testCube.py

import unittest
from . import cube

class TestCube(unittest.TestCase):
    def test_blue_center(self):
        myCube = cube.Cube()
        self.assertEqual(myCube.face['b'][4], 'b')


if __name__ == "__main__":
    unittest.main()


