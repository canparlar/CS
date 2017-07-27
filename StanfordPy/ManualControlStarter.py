'''
/* =======================================================================
   (c) 2015, Kre8 Technology, Inc.

   Name:          Joystick for Hamster
   By:            Qin Chen
   Last Updated:  4/10/17

   PROPRIETARY and CONFIDENTIAL
   ========================================================================*/
'''
import sys
import threading
import Tkinter as tk
import time  # sleep
from HamsterAPI.comm_ble import RobotComm
#for PC, need to import from commm_usb

gQuit = False

class SensorDisplayThread(threading.Thread):
    def __init__(self, canvas, robotList):
        super(SensorDisplayThread, self).__init__()
        self.robotList = robotList
        self.canvas = canvas
        ###########################################################
        # Display a blue rectangle in center of window, representing Hamster.
        # Create a line segment for left proximilty sensor display
        # Create a line segment for right proxijity sensor display
        # Creat a rectangle for displaying the left floor sensor 
        # Create a rectangle for displaying the right floor sensor
        ###########################################################
        return

    def run(self):   
        while not gQuit:
            if self.robotList:
                for robot in self.robotList:
                    ##############################
                    # Your code for displaying proximity sensors
                    ##############################
                    print "display prox sensors here"

                    ################################
                    # Your code for displaying floor sensors
                    ################################
                    print "display floor sensors here"
            else:
                print "waiting for robot"
            #time.sleep(0.1)

        for robot in self.robotList:
            robot.reset()
        return

class RobotMoves(object):
    def __init__(self, robotList):
        self.robotList = robotList
        return

    def move_up(self, event=None):
        if self.robotList:
            for robot in self.robotList:
                robot.set_wheel(0,30)
                robot.set_wheel(1,30)
        else:
            print "waiting for robot"

    def move_down(self, event=None):
        pass

    def move_left(self, event=None):
        pass

    def move_right(self, event=None):
        pass

    def stop_move(self, event=None):
        pass

class UI(object):
    def __init__(self, root, robot_moves):
        self.root = root
        self.robot_moves = robot_moves  # handle to robot commands
        self.canvas = None
        self.initUI()
        return

    def initUI(self):
        ###################################################################
        # Create a Hamster joystick window which contains
        # 1. a canvas where "sensor readings" are displayed
        # 2. a button for exit, i.e., a call to stopProg(), given in this class
        # 3. listen to key press and key release when focus is on this window
        ###################################################################
        pass
    
    ####################################################
    # Implement callback function when key press is detected
    ####################################################
    def keydown(self, event):
        pass

    #####################################################
    # Implement callback function when key release is detected
    #####################################################
    def keyup(self, event):
        pass

    def stopProg(self, event=None):
        global gQuit
        gQuit = True
        self.root.quit()    # close window
        return

def main(argv=None):
    gMaxRobotNum = 1; # max number of robots to control
    comm = RobotComm(gMaxRobotNum)
    comm.start()
    print 'Bluetooth starts'
    robotList = comm.robotList

    robot_moves = RobotMoves(robotList)
    m = tk.Tk() #root
    gui = UI(m, robot_moves)

    # start a watcher thread
    display=SensorDisplayThread(gui.canvas, robotList)
    display.setDaemon(True)
    display.start()
    
    m.mainloop()

    comm.stop()
    comm.join()

if __name__== "__main__":
    sys.exit(main())