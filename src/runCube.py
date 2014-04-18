# runCube.py

import cube

def main():
   testCube = cube.Cube()
   testCube.print_cube()
   print("Reorient left")
   testCube.reorient("left")
   print("front up")
   testCube.move("front","up")
   print("Reorient right")
   testCube.reorient("right")
   testCube.print_cube()
   


if __name__ == "__main__":
    main()
