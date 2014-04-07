# runCube.py

import cube

def main():
   testCube = cube.Cube()
   testCube.print_cube() 

   print("Front rup")
   testCube.move('front', 'rup')
   testCube.print_cube()
   print("Front bright")
   testCube.move('front', 'bright')
   testCube.print_cube()

if __name__ == "__main__":
    main()
