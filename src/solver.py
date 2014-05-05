# solver.py

import cube

class Solver(object):

    def __init__(self):
        pass

    def solve(self, target):
        target.move('front', 'rdown')
        target.move('front', 'bright')
        target.move('front', 'rup')

        return True
    
