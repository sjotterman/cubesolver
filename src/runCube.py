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

   print("Here's a new cube:")
   secondCube = cube.Cube()
   secondCube.print_cube()
   print("Reorient up")
   secondCube.reorient("up")
   secondCube.print_cube()
   print("Rotating the right side clockwise.")
   secondCube.move('right', 'cw') 
   secondCube.print_cube()
   print("Reorient up")
   secondCube.reorient("up")
   secondCube.print_cube()

if __name__ == "__main__":
    main()
