# testSolver.py

import unittest
from ..src import solver
from ..src import cube

class TestSolver(unittest.TestCase):

    def test_createSolver(self):
        mySolver = solver.Solver()

    def test_solveStartingCube(self):
        myCube = cube.Cube()
        mySolver = solver.Solver()
        self.assertEqual(myCube.is_solved(), True)
        self.assertEqual(mySolver.solve(), True)
        self.assertEqual(myCube.is_solved(), True)



