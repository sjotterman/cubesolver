# runCube.py

import cube

def main():
   testCube = cube.Cube()
   testCube.print_cube()
   testCube.reorient('up')
   testCube.move('front','down')
   testCube.move('front','bright')
   testCube.move('front','up')
   testCube.reorient('left')
   testCube.move('front','ccw')
   testCube.move('front','left')
   testCube.move('front','cw')
   testCube.reorient('right')
   testCube.move('front', 'left')
   testCube.move('front','ccw')
   testCube.move('middle', 'right')
   testCube.move('front', 'cw')

   print("Switch two blue cubes")
   testCube.print_cube()
   

print


if __name__ == "__main__":
    main()
