# runCube.py

import cube

def main():
   testCube = cube.Cube()
   testCube.print_cube() 

   print("Rotating the right side clockwise.")
   testCube.move('right','cw') 
   testCube.print_cube() 
   print("Rotating the right side clockwise.")
   testCube.move('right','cw') 
   testCube.print_cube() 
   print("Rotating the right side clockwise.")
   testCube.move('right','cw') 
   testCube.print_cube() 
   print("Rotating the right side clockwise.")
   testCube.move('right','cw') 
   testCube.print_cube() 

if __name__ == "__main__":
    main()
