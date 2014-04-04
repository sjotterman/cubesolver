# cube.py

import collections

class Cube(object):

    def __init__(self):
        self.face = collections.defaultdict(dict)
        self.face['b'][4] = 'b'
        #self.face = {'r','g','b','y','o','w'}
        #self.face['b'] = ['','','','','b','','','']

