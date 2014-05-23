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
        self.assertEqual(mySolver.solve(myCube), True)
        self.assertEqual(myCube.is_solved(), True)

    def testSolveOneRedCube(self):
        myCube = cube.Cube()
        mySolver = solver.Solver()
        self.assertEqual(myCube.isFirstLayerSolved('r'), True)
        myCube.move('front', 'rdown')
        myCube.move('front', 'bleft')
        myCube.move('front', 'rup')
        self.assertEqual(myCube.isFirstLayerSolved('r'), False)
        self.assertEqual(mySolver.solve(myCube), True)
        self.assertEqual(myCube.isFirstLayerSolved('r'), True)
    
    def testSolveThreeRedCubes(self):
        myCube = cube.Cube()
        mySolver = solver.Solver()
        self.assertEqual(myCube.isFirstLayerSolved('r'), True)
        myCube.move('front', 'rdown')
        self.assertEqual(myCube.isFirstLayerSolved('r'), False)
        self.assertEqual(mySolver.solve(myCube), True)
        self.assertEqual(myCube.isFirstLayerSolved('r'), True)
    
    def testSolveThreeRedCubes2(self):
        myCube = cube.Cube()
        mySolver = solver.Solver()
        self.assertEqual(myCube.isFirstLayerSolved('r'), True)
        myCube.move('front', 'rup')
        self.assertEqual(myCube.isFirstLayerSolved('r'), False)
        self.assertEqual(mySolver.solve(myCube), True)
        self.assertEqual(myCube.isFirstLayerSolved('r'), True)
    
    def testSolveThreeRedCubes3(self):
        myCube = cube.Cube()
        mySolver = solver.Solver()
        self.assertEqual(myCube.isFirstLayerSolved('r'), True)
        myCube.move('front', 'rup')
        self.assertEqual(myCube.isFirstLayerSolved('r'), False)
        self.assertEqual(mySolver.solve(myCube), True)
        self.assertEqual(myCube.isFirstLayerSolved('r'), True)
    
    def testSolveThreeRedCubes4(self):
        myCube = cube.Cube()
        mySolver = solver.Solver()
        self.assertEqual(myCube.isFirstLayerSolved('r'), True)
        myCube.reorient('left')
        myCube.move('front', 'up')
        myCube.reorient('right')
        self.assertEqual(myCube.isFirstLayerSolved('r'), False)
        self.assertEqual(mySolver.solve(myCube), True)
        self.assertEqual(myCube.isFirstLayerSolved('r'), True)

        

          


