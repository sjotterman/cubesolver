# testSolver.py

import unittest
from ..src import solver

class TestSolver(unittest.TestCase):
  def test_createSolver(self):
    mySolver = solver.Solver()

