# runCube.py

import cube

def main():
   testCube = cube.Cube()
   testCube.print_cube()
   print("reorient up")
   testCube.reorient('up')
   testCube.print_cube()
   print("Front down")
   testCube.move('front','down')
   testCube.print_cube()
   print("Front bright")
   testCube.move('front','bright')
   testCube.print_cube()
   print("front up")
   testCube.move('front','up')
   testCube.print_cube()
   print("reorient left")
   testCube.reorient('left')
   testCube.print_cube()
   print("front ccw")
   testCube.move('front','ccw')
   testCube.print_cube()
   print("front left")
   testCube.move('front','left')
   testCube.print_cube()
   print("front cw")
   testCube.move('front','cw')
   testCube.print_cube()
   print("reorient right")
   testCube.reorient('right')
   testCube.print_cube()
   print("front left")
   testCube.move('front', 'left')
   testCube.print_cube()
   print("front ccw")
   testCube.move('front','ccw')
   testCube.print_cube()
   print("middle right")
   testCube.move('middle', 'right')
   testCube.print_cube()
   print("front cw")
   testCube.move('front', 'cw')
   testCube.print_cube()

   print("Switch two blue cubes")
   testCube.print_cube()
   

print


if __name__ == "__main__":
    main()
