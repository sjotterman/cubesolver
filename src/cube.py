# cube.py

import collections

class Cube(object):

    def __init__(self):
        self.face = collections.defaultdict(dict)
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

    def move(self, face, dir):
        if dir == 'ccw':
            self.move(face, 'cw')
            self.move(face, 'cw')
            self.move(face, 'cw')
            return

        if dir == 'down':
            self.move(face, 'up')
            self.move(face, 'up')
            self.move(face, 'up')
            return

        if dir == 'ldown':
            self.move(face, 'lup')
            self.move(face, 'lup')
            self.move(face, 'lup')
            return

        if dir == 'rdown':
            self.move(face, 'rup')
            self.move(face, 'rup')
            self.move(face, 'rup')
            return

        face_front = self.face['front']
        face_bottom = self.face['bottom']
        face_back = self.face['back']
        face_top = self.face['top']
        face_right = self.face['right']
        face_left = self.face['left']

        if dir == 'cw':
            temp_square1 = face_front[2]
            temp_square2 = face_front[5]
            temp_square3 = face_front[8]

            face_front[2] = face_bottom[2]
            face_front[5] = face_bottom[5]
            face_front[8] = face_bottom[8]

            face_bottom[2] = face_back[2]
            face_bottom[5] = face_back[5]
            face_bottom[8] = face_back[8]

            face_back[2] = face_top[2]
            face_back[5] = face_top[5]
            face_back[8] = face_top[8]

            face_top[2] = temp_square1
            face_top[5] = temp_square2
            face_top[8] = temp_square3

        if dir == 'up':
            temp_square1 = face_front[1]
            temp_square2 = face_front[4]
            temp_square3 = face_front[7]

            face_front[1] = face_bottom[1]
            face_front[4] = face_bottom[4]
            face_front[7] = face_bottom[7]

            face_bottom[1] = face_back[1]
            face_bottom[4] = face_back[4]
            face_bottom[7] = face_back[7]

            face_back[1] = face_top[1]
            face_back[4] = face_top[4]
            face_back[7] = face_top[7]

            face_top[1] = temp_square1
            face_top[4] = temp_square2
            face_top[7] = temp_square3

        if dir == 'rup':
            temp_square1 = face_front[2]
            temp_square2 = face_front[5]
            temp_square3 = face_front[8]

            face_front[2] = face_bottom[2]
            face_front[5] = face_bottom[5]
            face_front[8] = face_bottom[8]

            face_bottom[2] = face_back[2]
            face_bottom[5] = face_back[5]
            face_bottom[8] = face_back[8]

            face_back[2] = face_top[2]
            face_back[5] = face_top[5]
            face_back[8] = face_top[8]

            face_top[2] = temp_square1
            face_top[5] = temp_square2
            face_top[8] = temp_square3

            # right side cw
            temp_square0 = face_right[0]
            temp_square1 = face_right[1]
            temp_square2 = face_right[2]
            face_right[0] = face_right[6]
            face_right[1] = face_right[3]
            face_right[2] = face_right[0]
            face_right[3] = face_right[7]
            face_right[6] = face_right[8]
            face_right[7] = face_right[5]
            face_right[8] = temp_square2
            face_right[5] = temp_square1
            face_right[2] = temp_square0

        if dir == 'lup':
            temp_square1 = face_front[0]
            temp_square2 = face_front[3]
            temp_square3 = face_front[6]

            face_front[0] = face_bottom[0]
            face_front[3] = face_bottom[3]
            face_front[6] = face_bottom[6]

            face_bottom[0] = face_back[0]
            face_bottom[3] = face_back[3]
            face_bottom[6] = face_back[6]

            face_back[0] = face_top[0]
            face_back[3] = face_top[3]
            face_back[6] = face_top[6]

            face_top[0] = temp_square1
            face_top[3] = temp_square2
            face_top[6] = temp_square3

            # left side ccw
            temp_square0 = face_left[6]
            temp_square1 = face_left[7]
            temp_square2 = face_left[8]
            face_left[0] = face_left[2]
            face_left[1] = face_left[5]
            face_left[2] = face_left[8]
            face_left[3] = face_left[1]
            face_left[6] = face_left[0]
            face_left[7] = face_left[3]
            face_left[8] = temp_square0
            face_left[5] = temp_square1

        if dir == 'right':
            temp_square1 = face_back[3]
            temp_square2 = face_back[4]
            temp_square3 = face_back[5]

            face_back[5] = face_right[3]
            face_back[4] = face_right[4]
            face_back[3] = face_right[5]

            face_right[3] = face_front[3]
            face_right[4] = face_front[4]
            face_right[5] = face_front[5]

            face_front[3] = face_left[3]
            face_front[4] = face_left[4]
            face_front[5] = face_left[5]

            face_left[5] = temp_square1
            face_left[4] = temp_square2
            face_left[3] = temp_square3

        if dir == 'tright':
            temp_square1 = face_back[8]
            temp_square2 = face_back[7]
            temp_square3 = face_back[6]

            face_back[8] = face_right[0]
            face_back[7] = face_right[1]
            face_back[6] = face_right[2]

            face_right[0] = face_front[0]
            face_right[1] = face_front[1]
            face_right[2] = face_front[2]

            face_front[0] = face_left[0]
            face_front[1] = face_left[1]
            face_front[2] = face_left[2]

            face_left[0] = temp_square1
            face_left[1] = temp_square2
            face_left[2] = temp_square3
            
            # top side ccw
            temp_square0 = face_top[6]
            temp_square1 = face_top[7]
            temp_square2 = face_top[8]
            face_top[0] = face_top[2]
            face_top[1] = face_top[5]
            face_top[2] = face_top[8]
            face_top[3] = face_top[1]
            face_top[6] = face_top[0]
            face_top[7] = face_top[3]
            face_top[8] = temp_square0
            face_top[5] = temp_square1

        if dir == 'bright':
            temp_square1 = face_back[2]
            temp_square2 = face_back[1]
            temp_square3 = face_back[0]

            face_back[0] = face_right[8]
            face_back[1] = face_right[7]
            face_back[2] = face_right[6]

            face_right[6] = face_front[6]
            face_right[7] = face_front[7]
            face_right[8] = face_front[8]

            face_front[6] = face_left[6]
            face_front[7] = face_left[7]
            face_front[8] = face_left[8]

            face_left[6] = temp_square1
            face_left[7] = temp_square2
            face_left[8] = temp_square3



    def reorient(self, direction):
        if direction == 'down':
            self.reorient('up')
            self.reorient('up')
            self.reorient('up')
            return
        
        if direction == 'up':
            self.move('front','lup')
            self.move('front','up')
            self.move('front','rup')
        
        if direction == 'right':
            self.move('front','tright')
            self.move('front','right')
            self.move('fromt','bright')

    def print_cube(self):
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
