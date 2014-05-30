# solver.py

import cube

class Solver(object):

    def __init__(self):
        pass

    def solve(self, target):
        topColor = target.face['top'][4]
        rightColor = target.face['right'][4]
        frontColor = target.face['front'][4]
        leftColor = target.face['left'][4]
        backColor = target.face['back'][4]
        loopCounter = 0
        while target.isFirstLayerSolved(topColor) == False:
            #print("beginning of while loop")
            for i in range(0,4):
                #print("i = " + str(i))
                #target.print_cube()
                #print("Front bleft")
                target.move('front', 'bleft')
                
                # front bottom left square needs to go to top 
                if target.face['front'][6] == topColor:
                    if (target.face['left'][8] == leftColor) \
                        and (target.face['bottom'][0] == frontColor):
                        target.move('front', 'bright')
                        target.move('front', 'ldown')
                        target.move('front', 'bleft')
                        target.move('front', 'lup')
                # front bottom right square needs to go to top 
                elif target.face['front'][8] == topColor:
                    if (target.face['right'][6] == rightColor) \
                        and (target.face['bottom'][2] == frontColor):
                        target.move('front', 'bleft')
                        target.move('front', 'rdown')
                        target.move('front', 'bright')
                        target.move('front', 'rup')
                    #stuff
                # front bottom middle square needs to go to top 
                elif target.face['front'][7] == topColor:
                    if (target.face['bottom'][1] == frontColor):
                        target.move('front', 'bright')
                        target.move('front', 'down')
                        target.move('front', 'bleft')
                        target.move('front', 'up')
                            
                # bottom top left square needs to go to top 
                elif target.face['bottom'][0] == topColor:
                    if (target.face['left'][8] == frontColor) \
                        and (target.face['front'][6] == leftColor):
                        target.move('front', 'ldown')
                        target.move('front', 'bright')
                        target.move('front', 'bright')
                        target.move('front', 'lup')
                        target.move('front', 'bleft')
                        target.move('front', 'ldown')
                        target.move('front', 'bright')
                        target.move('front', 'lup')


                # bottom top middle square needs to go to top 
                elif target.face['bottom'][1] == topColor:
                    if target.face['front'][6] == frontColor:
                        target.move('front', 'ccw')
                        target.move('front', 'right')
                        target.move('front', 'ccw')
                        target.move('front', 'ccw')
                        target.move('front', 'left')
                        target.move('front', 'ccw')

                # bottom top right square needs to go to top 
                elif target.face['bottom'][2] == topColor:
                    if (target.face['right'][6] == frontColor) \
                        and (target.face['front'][8] == rightColor):
                        target.move('front', 'rdown')
                        target.move('front', 'bleft')
                        target.move('front', 'bleft')
                        target.move('front', 'rup')
                        target.move('front', 'bright')
                        target.move('front', 'rdown')
                        target.move('front', 'bleft')
                        target.move('front', 'rup')
                
                # front top right square needs to go to top, just rotate it
                # down, it will be handled
                elif target.face['front'][2] == topColor:
                    target.move('front', 'rdown')
                    target.move('front', 'bleft')
                    target.move('front', 'rup')
                # front left right square needs to go to top, just rotate it
                # down, it will be handled
                elif target.face['front'][0] == topColor:
                    target.move('front', 'ldown')
                    target.move('front', 'bright')
                    target.move('front', 'lup')
                # top face square is not in right position
                elif target.face['front'][1] == topColor  \
                    and target.face['top'][7] == frontColor:
                    target.move('front', 'ccw')
                    target.move('front', 'right')
                    target.move('front', 'right')
                    target.move('front', 'ccw')
                    target.move('front', 'ccw')
                    target.move('front', 'left')
                    target.move('front', 'cw')
                # this will need to be refactored
                else:
                    if target.face['top'][6] == topColor:
                        if target.face['front'][0] != frontColor \
                            or target.face['left'][2] != leftColor:
                            target.move('front','ldown')
                            target.move('front', 'bright')
                            target.move('front', 'lup')
                    if target.face['top'][7] == topColor:
                        if target.face['front'][1] != frontColor:
                            target.move('front','down')
                            target.move('front', 'bright')
                            target.move('front', 'up')
                    if target.face['top'][8] == topColor:
                        if target.face['front'][2] != frontColor \
                            or target.face['right'][0] != rightColor:
                            target.move('front','rdown')
                            target.move('front', 'bleft')
                            target.move('front', 'rup')

            for j in range(0, 4):
                if target.face['front'][3] == topColor \
                    and target.face['left'][5] == target.face['front'][0]:
                    target.move('front', 'right')
                    target.move('front', 'right')
                    target.move('front', 'cw')
                    target.move('front', 'left')
                    target.move('front', 'ccw')
                elif target.face['front'][5] == topColor \
                and target.face['right'][3] == target.face['front'][0]:
                    target.move('front', 'right')
                    target.move('front', 'ccw')
                    target.move('front', 'left')
                    target.move('front', 'left')
                    target.move('front', 'cw')
                target.move('front', 'left')
                





            target.reorient('left')
            #target.print_cube()
            #print("Reorient left")
            topColor = target.face['top'][4]
            rightColor = target.face['right'][4]
            frontColor = target.face['front'][4]
            leftColor = target.face['left'][4]
            backColor = target.face['back'][4]
            loopCounter += 1

            if loopCounter == 4000:
                print ("Loop Counter exceeded 4000.")
                target.print_cube()
                return False

        return True
    
