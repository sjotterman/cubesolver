# cube.py

import collections

class Cube(object):

    def __init__(self):
        self.face = collections.defaultdict(dict)
        for key in ['r','b','y','o','w','g']:
            for i in range(0,9):
                self.face[key][i] = key

