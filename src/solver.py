# solver.py

import cube

class Solver(object):

    def __init__(self):
        pass

    def solve(self, target):
        if (target.face['top'][2] == 'g'):
            target.move('front', 'rup')
            return True

        if (target.face['top'][2] == 'b'):
            target.move('front', 'rdown')
            return True

        if (target.face['top'][4] == 'w'):
            target.reorient('left')
            target.move('front', 'down')
            target.reorient('right')
            return True

        if (target.face['top'][7] == 'w'):
            target.move('front', 'down')
            target.move('front', 'bright')
            target.move('front', 'up')
            return True

        target.move('front', 'rdown')
        target.move('front', 'bright')
        target.move('front', 'rup')

        return True
    
