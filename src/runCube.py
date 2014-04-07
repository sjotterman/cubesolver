# runCube.py

import cube

def main():
   testCube = cube.Cube()
   testCube.print_cube()
   print("front lup")
   testCube.move('front', 'lup')
   testCube.print_cube()
   print("front right")
   testCube.move('front', 'right')
   testCube.print_cube()
   

print


if __name__ == "__main__":
    main()
