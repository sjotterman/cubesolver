# runCube.py

import cube

def main():
   testCube = cube.Cube()
   testCube.print_cube()
   print("Front tright")
   testCube.move('front','tright')
   testCube.print_cube()
   print("Front down")
   testCube.move('front','down')
   testCube.print_cube()
   print("Front left")
   testCube.move('front','left')
   testCube.print_cube()



if __name__ == "__main__":
    main()
