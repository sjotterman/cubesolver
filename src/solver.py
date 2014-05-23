# solver.py

import cube

class Solver(object):

    def __init__(self):
        pass

    def solve(self, target):
        if (target.face['top'][2] == 'g'):
            target.move('front', 'rup')
            return True

        target.move('front', 'rdown')
        target.move('front', 'bright')
        target.move('front', 'rup')

        return True
    
