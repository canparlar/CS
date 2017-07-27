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
import time
from HamsterAPI.comm_ble import RobotComm


gQuit = False

class SensorDisplayThread(threading.Thread):
    def __init__(self, canvas, robotList):
        super(SensorDisplayThread, self).__init__()
        self.robotList = robotList
        self.canvas = canvas
        ###########################################################
        # DONE Display a blue rectangle in center of window, representing Hamster.
        # DONE Create a line segment for left proximilty sensor display
        # DONE Create a line segment for right proxijity sensor display
        # DONE Creat a rectangle for displaying the left floor sensor 
        # DONE Create a rectangle for displaying the right floor sensor
        ###########################################################
        self.hams = (170,170,230,230)
        self.hams_id = self.canvas.create_rectangle(self.hams, fill = "white")
        self.lprox = (185,170,185,170)
        self.lprox_id = self.canvas.create_line(self.lprox, fill = "blue")
        self.rprox = (215,170,215,170)
        self.rprox_id = self.canvas.create_line(self.rprox, fill = "blue")
        self.lfloor = (180,180,190,185)
        self.lfloor_id = self.canvas.create_rectangle(self.lfloor, fill = "blue")
        self.rfloor = (220,220,210,215)
        self.rfloor_id = self.canvas.create_rectangle(self.rfloor, fill = "blue")
        print "done initializing sensor display thread"
        return

    def run(self):   
        while not gQuit:
            if self.robotList:
                for robot in self.robotList:
                    ##############################
                    # Your code for displaying proximity sensors
                    ##############################
                    lproxv = robot.get_proximity(0)
                    rproxv = robot.get_proximity(1)
                    if rproxv > 0 and lproxv > 0:
                        n_rprox = (1/float(rproxv))*1000
                        n_lprox = (1/float(lproxv))*1000
                    else:
                        n_rprox = 0
                        n_lprox = 0
                    self.canvas.itemconfig(self.lprox_id, fill = "red")
                    self.canvas.itemconfig(self.rprox_id, fill = "red")
                    self.canvas.coords(self.lprox_id,(185,170-n_lprox,185,170))
                    self.canvas.coords(self.rprox_id,(215,170-n_rprox,215,170))
                        

                    ################################
                    # DONE Your code for displaying floor sensors
                    ################################
                    lfloorv = robot.get_floor(0) 
                    rfloorv = robot.get_floor(1)
                    if lfloorv > 50:
                        self.canvas.itemconfig(self.lfloor_id, fill = "White")
                    else:
                        self.canvas.itemconfig(self.lfloor_id, fill = "Black")
                    if rfloorv > 50:
                        self.canvas.itemconfig(self.rfloor_id, fill = "White")
                    else:
                        self.canvas.itemconfig(self.rfloor_id, fill = "Black")
            else:
                print "waiting for robot"
            time.sleep(0.01)

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
                robot.set_wheel(0,100)
                robot.set_wheel(1,100)
        else:
            print "waiting for robot"

    def move_down(self, event=None):
        if self.robotList:
            for robot in self.robotList:
                robot.set_wheel(0,-100)
                robot.set_wheel(1,-100)
        else:
            print "waiting for robot"

    def move_left(self, event=None):
        if self.robotList:
            for robot in self.robotList:
                robot.set_wheel(0,100)
                robot.set_wheel(1,-100)
        else:
            print "waiting for robot"

    def move_right(self, event=None):
        if self.robotList:
            for robot in self.robotList:
                robot.set_wheel(0,-100)
                robot.set_wheel(1,100)
        else:
            print "waiting for robot"

    def stop_move(self, event=None):
        if self.robotList:
            for robot in self.robotList:
                robot.set_wheel(0,0)
                robot.set_wheel(1,0)
        else:
            print "waiting for robot"

class UI(object):
    def __init__(self, root, robot_moves):
        self.root = root
        self.robot_moves = robot_moves  # handle to robot commands
        self.canvas = None
        self.initUI()
        return

    def initUI(self):
        ###################################################################
        # DONE? Create a Hamster joystick window which contains
        # DONE? 1.a canvas where "sensor readings" are displayed
        # DONE 2. a button for exit, i.e., a call to stopProg(), given in this class
        # DONE 3. listen to key press and key release when focus is on this window
        ###################################################################
        self.canvas = tk.Canvas(self.root, bg="Blue",height=400,width=400)
        self.canvas.pack()
        b1 = tk.Button(self.root, text='Exit',command = self.stopProg())
        b1.pack(side='left')
        b1.bind('<Button-1>', self.stopProg)
        self.root.bind('<KeyPress>', self.keydown)
    
    ####################################################
    # DONE Implement callback function when key press is detected
    ####################################################
    def keydown(self, event):
        if event.char == 'w':
            self.robot_moves.move_up(event)
        if event.char == 'a':
            self.robot_moves.move_right(event)
        if event.char == 's':
            self.robot_moves.move_down(event)
        if event.char == 'd':
            self.robot_moves.move_left(event)
        self.root.bind('<KeyRelease>', self.keyup)
    #####################################################
    # DONE Implement callback function when key release is detected
    #####################################################
    def keyup(self, event):
       self.robot_moves.stop_move(event)


    def stopProg(self, event=None):
        
        gQuit = True
        self.root.quit()    # close window
        return

def main(argv=None):
    gMaxRobotNum = 1; # max number of robots to control
    comm = RobotComm(gMaxRobotNum)
    comm.start()
    print 'Bluetooth starts'
    robotList = comm.robotList
    global gQuit 
    gQuit = False
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