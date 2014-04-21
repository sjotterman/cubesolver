# runCube.py

import cube

def main():
   testCube = cube.Cube()
   testCube.print_cube()
   count = 0
   while testCube.face['top'][4] != 'w' and count < 14: 
     if count == 4:
      testCube.reorient('up')
      testCube.print_cube()
     else:
      testCube.reorient('left')
      testCube.print_cube()
     count += 1



if __name__ == "__main__":
    main()
