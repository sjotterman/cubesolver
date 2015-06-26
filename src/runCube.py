# runCube.py

import cube
import solver


def main():
    myCube = cube.Cube()
    mySolver = solver.Solver()
    myCube.print_cube()
    for i in range(0, 4):
        myCube.move('front', 'rdown')
        myCube.move('front', 'bleft')
        myCube.move('front', 'rup')
        myCube.move('front', 'bright')
        myCube.move('front', 'rdown')
        myCube.move('front', 'bleft')
        myCube.move('front', 'rup')
        myCube.reorient('left')
    myCube.print_cube()
    print("Solving..")
    mySolver.solve(myCube)
    myCube.print_cube()


if __name__ == "__main__":
    main()
