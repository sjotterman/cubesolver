# cube.py

import collections

class Cube(object):

    def __init__(self):
        self.face = collections.defaultdict(dict)
        ##for key in ['r','b','y','o','w','g']:
            ##for i in range(0,9):
                ##self.face[key][i] = key
        self.setup_face('front', 'b')
        self.setup_face('top', 'r')
        self.setup_face('left', 'y')
        self.setup_face('bottom', 'o')
        self.setup_face('right', 'w')
        self.setup_face('back', 'g')

    def setup_face(self, face, color):
        for i in range(0,9):
            self.face[face][i] = color;

    def is_solved(self):
        return True;

    def print_cube(self):
        print("This will eventually print the cube faces.")
        
        # top side
        print("   " + 
             self.face['top'][0] +
             self.face['top'][1] +
             self.face['top'][2] + "   ");
        print("   " + 
             self.face['top'][3] +
             self.face['top'][4] +
             self.face['top'][5] + "   ");
        print("   " + 
             self.face['top'][6] +
             self.face['top'][7] +
             self.face['top'][8] + "   ");

        # left, front, and right sides
        print( 
             self.face['left'][0] +
             self.face['left'][1] +
             self.face['left'][2] +
             self.face['front'][0] +
             self.face['front'][1] +
             self.face['front'][2] +
             self.face['right'][0] +
             self.face['right'][1] +
             self.face['right'][2]);
        print( 
             self.face['left'][3] +
             self.face['left'][4] +
             self.face['left'][5] +
             self.face['front'][3] +
             self.face['front'][4] +
             self.face['front'][5] +
             self.face['right'][3] +
             self.face['right'][4] +
             self.face['right'][5]);
        print( 
             self.face['left'][6] +
             self.face['left'][7] +
             self.face['left'][7] +
             self.face['front'][6] +
             self.face['front'][7] +
             self.face['front'][8] +
             self.face['right'][6] +
             self.face['right'][7] +
             self.face['right'][8]);

       #bottom side 
        print("   " + 
             self.face['bottom'][0] +
             self.face['bottom'][1] +
             self.face['bottom'][2] + "   ");
        print("   " + 
             self.face['bottom'][3] +
             self.face['bottom'][4] +
             self.face['bottom'][5] + "   ");
        print("   " + 
             self.face['bottom'][6] +
             self.face['bottom'][7] +
             self.face['bottom'][8] + "   ");

        # back side
        print("   " + 
             self.face['back'][0] +
             self.face['back'][1] +
             self.face['back'][2] + "   ");
        print("   " + 
             self.face['back'][3] +
             self.face['back'][4] +
             self.face['back'][5] + "   ");
        print("   " + 
             self.face['back'][6] +
             self.face['back'][7] +
             self.face['back'][8] + "   ");
