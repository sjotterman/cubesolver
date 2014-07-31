# runCube.py

import cube
import solver


def main():
    myCube = cube.Cube()
    mySolver = solver.Solver()
    myCube.print_cube()
    myCube.move('front', 'up')
    myCube.move('front', 'up')
    myCube.move('front', 'right')
    myCube.move('front', 'right')
    myCube.reorient('right')
    myCube.move('front', 'up')
    myCube.move('front', 'up')
    myCube.print_cube()
    print("Solving..")
    mySolver.solve(myCube)
    myCube.print_cube()


if __name__ == "__main__":
    main()
