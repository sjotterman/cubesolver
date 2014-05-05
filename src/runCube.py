# runCube.py

import cube

def main():
   myCube = cube.Cube()
   myCube.print_cube()
   myCube.move('front', 'rdown')
   myCube.print_cube()
   myCube.move('front', 'bleft')
   myCube.print_cube()
   myCube.move('front', 'rup')
   myCube.print_cube()


if __name__ == "__main__":
    main()
