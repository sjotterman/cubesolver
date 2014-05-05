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

        if dir == 'left':
            self.move(face, 'right')
            self.move(face, 'right')
            self.move(face, 'right')
            return

        if dir == 'bleft':
            self.move(face, 'bright')
            self.move(face, 'bright')
            self.move(face, 'bright')
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

        if face == 'right':
            self.reorient('left')
            self.move('front', dir)
            self.reorient('right')
            return

        face_front = self.face['front']
        face_bottom = self.face['bottom']
        face_back = self.face['back']
        face_top = self.face['top']
        face_right = self.face['right']
        face_left = self.face['left']

        if dir == 'cw':
            self.reorient('right')
            self.move('front', 'rup')
            self.reorient('left')
            return

        if dir == 'up':
            self.front_cubes_up('middle')

        if dir == 'rup':
            self.front_cubes_up('right')

            # right side cw
            self.rotate_face('right','cw')

        if dir == 'lup':
            self.front_cubes_up('left')

            # left side ccw
            self.rotate_face('left','ccw')

        if dir == 'right':
            self.front_cubes_right('middle')

        if dir == 'tright':
            self.front_cubes_right('top')
            
            # top side ccw
            self.rotate_face('top','ccw')

        if dir == 'bright':
            self.front_cubes_right('bottom')
            
            # bottom side cw
            self.rotate_face('bottom', 'cw')

    def rotate_face(self, face, dir):
        if dir == 'ccw':
            self.rotate_face(face,'cw')
            self.rotate_face(face,'cw')
            self.rotate_face(face,'cw')
            return

        temp_face = self.face[face]

        temp_square0 = temp_face[0]
        temp_square1 = temp_face[1]
        temp_square2 = temp_face[2]
        temp_face[0] = temp_face[6]
        temp_face[1] = temp_face[3]
        temp_face[2] = temp_face[0]
        temp_face[3] = temp_face[7]
        temp_face[6] = temp_face[8]
        temp_face[7] = temp_face[5]
        temp_face[8] = temp_square2
        temp_face[5] = temp_square1
        temp_face[2] = temp_square0

    def front_cubes_up(self, column):
        # default : middle column
        pos1 = 1
        pos2 = 4
        pos3 = 7
        if column == 'left':
            pos1 = 0
            pos2 = 3
            pos3 = 6
        if column == 'right':
            pos1 = 2
            pos2 = 5
            pos3 = 8
            
        temp_square1 = self.face['front'][pos1]
        temp_square2 = self.face['front'][pos2]
        temp_square3 = self.face['front'][pos3]

        self.face['front'][pos1] = self.face['bottom'][pos1]
        self.face['front'][pos2] = self.face['bottom'][pos2]
        self.face['front'][pos3] = self.face['bottom'][pos3]

        self.face['bottom'][pos1] = self.face['back'][pos1]
        self.face['bottom'][pos2] = self.face['back'][pos2]
        self.face['bottom'][pos3] = self.face['back'][pos3]

        self.face['back'][pos1] = self.face['top'][pos1]
        self.face['back'][pos2] = self.face['top'][pos2]
        self.face['back'][pos3] = self.face['top'][pos3]

        self.face['top'][pos1] = temp_square1
        self.face['top'][pos2] = temp_square2
        self.face['top'][pos3] = temp_square3

    def front_cubes_right(self, row):
        pos1 = 3
        pos2 = 4
        pos3 = 5
        backpos1 = 3
        backpos2 = 4
        backpos3 = 5
        if row == 'top':
            pos1 = 0
            pos2 = 1
            pos3 = 2
            backpos1 = 6
            backpos2 = 7
            backpos3 = 8

        if row == 'bottom':
            pos1 = 6
            pos2 = 7
            pos3 = 8
            backpos1 = 0
            backpos2 = 1
            backpos3 = 2
        temp_square1 = self.face['back'][backpos3]
        temp_square2 = self.face['back'][backpos2]
        temp_square3 = self.face['back'][backpos1]

        self.face['back'][backpos1] = self.face['right'][pos3]
        self.face['back'][backpos2] = self.face['right'][pos2]
        self.face['back'][backpos3] = self.face['right'][pos1]

        self.face['right'][pos1] = self.face['front'][pos1]
        self.face['right'][pos2] = self.face['front'][pos2]
        self.face['right'][pos3] = self.face['front'][pos3]

        self.face['front'][pos1] = self.face['left'][pos1]
        self.face['front'][pos2] = self.face['left'][pos2]
        self.face['front'][pos3] = self.face['left'][pos3]

        self.face['left'][pos1] = temp_square1
        self.face['left'][pos2] = temp_square2
        self.face['left'][pos3] = temp_square3

        
    def reorient(self, direction):
        if direction == 'down':
            self.reorient('up')
            self.reorient('up')
            self.reorient('up')
            return
        
        if direction == 'left':
            self.reorient('right')
            self.reorient('right')
            self.reorient('right')
            return

        if direction == 'up':
            self.move('front','lup')
            self.move('front','up')
            self.move('front','rup')
        
        if direction == 'right':
            self.move('front','tright')
            self.move('front','right')
            self.move('fromt','bright')

        if direction == 'cw':
            self.reorient('left')
            self.reorient('down')
            self.reorient('right')

        if direction == 'ccw':
            self.reorient('left')
            self.reorient('up')
            self.reorient('right')

    def print_cube(self):
        # top side
        print("\n\n***********************************")
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
             self.face['left'][8] +
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
        print("***********************************\n\n")

    def solved_status(self):
        status = 100.0
        total_complete = 0
        for face in ('front','top','bottom','left', 'right','back'):
            color = self.face[face][4]
            face_complete = 0
            for i in range(0,9):
               if self.face[face][i] == color:
                    face_complete += 1
            total_complete += face_complete
        status = (total_complete / 54.0) * 100
        return status

    def isFirstLayerSolved(self, start_color):
      status = True
      firstLayerFace = 'front'
      start_front = self.face['front'][4]
      start_top = self.face['top'][4]
      count = 0
      while self.face['top'][4] != start_color:
        if count == 4:
          self.reorient('left')
        else:
          self.reorient('up')
        count += 1
      left_face_color = self.face['left'][0]
      front_face_color = self.face['front'][0]
      right_face_color = self.face['right'][0]
      back_face_color = self.face['back'][8]
      for i in range(1,3):
        if self.face['left'][i] != left_face_color:
          status = False
        if self.face['front'][i] != front_face_color:
          status = False
        if self.face['right'][i] != right_face_color:
          status = False
        if self.face['back'][8 - i] != back_face_color:
          status = False
      while self.face['top'][4] != start_top:
        if count == 4:
          self.reorient('left')
        else:
          self.reorient('up')
        count += 1
      while self.face['front'][4] != start_front:
          self.reorient('left')

      return status

    def isThirdLayerSolved(self, start_color):
      status = True
      firstLayerFace = 'front'
      start_front = self.face['front'][4]
      start_top = self.face['top'][4]
      count = 0
      while self.face['top'][4] != start_color:
        if count == 4:
          self.reorient('left')
        else:
          self.reorient('up')
        count += 1
      left_face_color = self.face['left'][6]
      front_face_color = self.face['front'][6]
      right_face_color = self.face['right'][6]
      back_face_color = self.face['back'][0]
      for i in range(7,9):
        if self.face['left'][i] != left_face_color:
          status = False
        if self.face['front'][i] != front_face_color:
          status = False
        if self.face['right'][i] != right_face_color:
          status = False
        if self.face['back'][8 - i] != back_face_color:
          status = False
      while self.face['top'][4] != start_top:
        if count == 4:
          self.reorient('left')
        else:
          self.reorient('up')
        count += 1
      while self.face['front'][4] != start_front:
          self.reorient('left')

      return status

    def isSecondLayerSolved(self, start_color):
        status = True
        start_front = self.face['front'][4]
        start_top = self.face['top'][4]
        count = 0
        while self.face['top'][4] != start_color:
          if count == 4:
            self.reorient('left')
          else:
            self.reorient('up')
          count += 1
        left_face_color = self.face['left'][4]
        front_face_color = self.face['front'][4]
        right_face_color = self.face['right'][4]
        back_face_color = self.face['back'][4]
        for i in range(3,6):
            if self.face['left'][i] != left_face_color:
                status = False
            if self.face['front'][i] != front_face_color:
                status = False
            if self.face['right'][i] != right_face_color:
                status = False
            if self.face['back'][8 - i] != back_face_color:
                status = False
        while self.face['top'][4] != start_top:
          if count == 4:
            self.reorient('left')
          else:
            self.reorient('up')
          count += 1
        while self.face['front'][4] != start_front:
            self.reorient('left')

        return status
