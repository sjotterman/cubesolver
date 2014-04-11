# runCube.py

import cube

def main():
   testCube = cube.Cube()
   testCube.print_cube()
   print(testCube.solvedStatus())
   print("front rup")
   testCube.move('front', 'rup')
   testCube.print_cube()
   testCube.solvedStatus()
   

print


if __name__ == "__main__":
    main()
