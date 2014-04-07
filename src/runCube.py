# runCube.py

import cube

def main():
   testCube = cube.Cube()
   testCube.print_cube() 

   testCube.print_cube()
   print("front rup")
   testCube.move('front', 'rup')
   testCube.print_cube()
   print("front tright")
   testCube.move('front', 'tright')
   testCube.print_cube()

if __name__ == "__main__":
    main()
