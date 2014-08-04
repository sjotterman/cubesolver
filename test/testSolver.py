# testSolver.py

import unittest
from ..src import solver
from ..src import cube


class TestSolver(unittest.TestCase):

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

    def testSolveOneRedCube2(self):
        myCube = cube.Cube()
        mySolver = solver.Solver()
        self.assertEqual(myCube.isFirstLayerSolved('r'), True)
        myCube.move('front', 'down')
        myCube.move('front', 'bleft')
        myCube.move('front', 'up')
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
        self.assertEqual(myCube.isFirstLayerSolved('w'), True)

    def testSolveDoesNotReorient1(self):
        myCube = cube.Cube()
        mySolver = solver.Solver()
        myCube.reorient('left')
        myCube.move('front', 'up')
        myCube.reorient('right')
        originalTopColor = myCube.face['top'][4]
        originalFrontColor = myCube.face['front'][4]
        self.assertEqual(mySolver.solve(myCube), True)
        self.assertEqual(originalTopColor, myCube.face['top'][4])
        self.assertEqual(originalFrontColor, myCube.face['front'][4])

    def testSolveDoesNotReorient2(self):
        myCube = cube.Cube()
        mySolver = solver.Solver()
        myCube.move('front', 'up')
        myCube.move('front', 'right')
        originalTopColor = myCube.face['top'][4]
        originalFrontColor = myCube.face['front'][4]
        self.assertEqual(mySolver.solve(myCube), True)
        self.assertEqual(originalTopColor, myCube.face['top'][4])
        self.assertEqual(originalFrontColor, myCube.face['front'][4])

    def testSolveSwitchedCenters(self):
        myCube = cube.Cube()
        mySolver = solver.Solver()
        self.assertEqual(myCube.isFirstLayerSolved('r'), True)

        myCube.move('front', 'up')
        myCube.move('front', 'up')
        myCube.move('front', 'right')
        myCube.move('front', 'right')
        myCube.reorient('right')
        myCube.move('front', 'up')
        myCube.move('front', 'up')

        self.assertEqual(myCube.isFirstLayerSolved('r'), False)
        self.assertEqual(mySolver.solve(myCube), True)
        self.assertEqual(myCube.isFirstLayerSolved('r'), True)

    def testSolveMiddleCubes(self):
        myCube = cube.Cube()
        mySolver = solver.Solver()
        self.assertEqual(myCube.isSecondLayerSolved('r'), True)

        myCube.move('front', 'up')
        myCube.move('front', 'up')
        myCube.move('front', 'right')
        myCube.move('front', 'right')
        myCube.reorient('right')
        myCube.move('front', 'up')
        myCube.move('front', 'up')

        self.assertEqual(myCube.isSecondLayerSolved('r'), False)
        self.assertEqual(mySolver.solve(myCube), True)
        self.assertEqual(myCube.isSecondLayerSolved('r'), True)

    def testSwitchThreeEdgeCubesRedCCW1(self):
        myCube = cube.Cube()
        mySolver = solver.Solver()
        mySolver.switchThreeEdges(myCube, 'red', 1, 'ccw')
        self.assertEqual(myCube.isSecondLayerSolved('r'), True)
        self.assertEqual(myCube.face['top'][0], 'r')
        self.assertEqual(myCube.face['top'][1], 'w')
        self.assertEqual(myCube.face['top'][2], 'r')
        self.assertEqual(myCube.face['top'][3], 'g')
        self.assertEqual(myCube.face['top'][4], 'r')
        self.assertEqual(myCube.face['top'][5], 'r')
        self.assertEqual(myCube.face['top'][6], 'r')
        self.assertEqual(myCube.face['top'][7], 'r')
        self.assertEqual(myCube.face['top'][8], 'r')
        self.assertEqual(myCube.face['left'][0], 'y')
        self.assertEqual(myCube.face['left'][1], 'r')
        self.assertEqual(myCube.face['left'][2], 'y')
        self.assertEqual(myCube.face['front'][0], 'b')
        self.assertEqual(myCube.face['front'][1], 'b')
        self.assertEqual(myCube.face['front'][2], 'b')
        self.assertEqual(myCube.face['right'][0], 'w')
        self.assertEqual(myCube.face['right'][1], 'y')
        self.assertEqual(myCube.face['right'][2], 'w')
        self.assertEqual(myCube.face['back'][6], 'g')
        self.assertEqual(myCube.face['back'][7], 'r')
        self.assertEqual(myCube.face['back'][8], 'g')

    def testSwitchThreeEdgeCubesRedCCW2(self):
        myCube = cube.Cube()
        mySolver = solver.Solver()
        mySolver.switchThreeEdges(myCube, 'red', 3, 'ccw')
        self.assertEqual(myCube.isSecondLayerSolved('r'), True)
        self.assertEqual(myCube.face['top'][0], 'r')
        self.assertEqual(myCube.face['top'][1], 'r')
        self.assertEqual(myCube.face['top'][2], 'r')
        self.assertEqual(myCube.face['top'][3], 'g')
        self.assertEqual(myCube.face['top'][4], 'r')
        self.assertEqual(myCube.face['top'][5], 'r')
        self.assertEqual(myCube.face['top'][6], 'r')
        self.assertEqual(myCube.face['top'][7], 'y')
        self.assertEqual(myCube.face['top'][8], 'r')
        self.assertEqual(myCube.face['left'][0], 'y')
        self.assertEqual(myCube.face['left'][1], 'r')
        self.assertEqual(myCube.face['left'][2], 'y')
        self.assertEqual(myCube.face['front'][0], 'b')
        self.assertEqual(myCube.face['front'][1], 'r')
        self.assertEqual(myCube.face['front'][2], 'b')
        self.assertEqual(myCube.face['right'][0], 'w')
        self.assertEqual(myCube.face['right'][1], 'w')
        self.assertEqual(myCube.face['right'][2], 'w')
        self.assertEqual(myCube.face['back'][6], 'g')
        self.assertEqual(myCube.face['back'][7], 'b')
        self.assertEqual(myCube.face['back'][8], 'g')

    def testSwitchThreeEdgeCubesRedCCW3(self):
        myCube = cube.Cube()
        mySolver = solver.Solver()
        mySolver.switchThreeEdges(myCube, 'red', 5, 'ccw')
        self.assertEqual(myCube.isSecondLayerSolved('r'), True)
        self.assertEqual(myCube.face['top'][0], 'r')
        self.assertEqual(myCube.face['top'][1], 'w')
        self.assertEqual(myCube.face['top'][2], 'r')
        self.assertEqual(myCube.face['top'][3], 'r')
        self.assertEqual(myCube.face['top'][4], 'r')
        self.assertEqual(myCube.face['top'][5], 'b')
        self.assertEqual(myCube.face['top'][6], 'r')
        self.assertEqual(myCube.face['top'][7], 'r')
        self.assertEqual(myCube.face['top'][8], 'r')
        self.assertEqual(myCube.face['left'][0], 'y')
        self.assertEqual(myCube.face['left'][1], 'y')
        self.assertEqual(myCube.face['left'][2], 'y')
        self.assertEqual(myCube.face['front'][0], 'b')
        self.assertEqual(myCube.face['front'][1], 'g')
        self.assertEqual(myCube.face['front'][2], 'b')
        self.assertEqual(myCube.face['right'][0], 'w')
        self.assertEqual(myCube.face['right'][1], 'r')
        self.assertEqual(myCube.face['right'][2], 'w')
        self.assertEqual(myCube.face['back'][6], 'g')
        self.assertEqual(myCube.face['back'][7], 'r')
        self.assertEqual(myCube.face['back'][8], 'g')
