'''
/* =======================================================================
   (c) 2015, Kre8 Technology, Inc.
   This is a program that is provided to students in Robot AI class.
   Students use this it to build different Hamster behaviors.

   Name:          starter1.py
   By:            Qin Chen
   Last Updated:  6/10/16

   PROPRIETARY and CONFIDENTIAL
   ========================================================================*/
'''
import sys
import time
import threading
import Tkinter as tk
from HamsterAPI.comm_ble import RobotComm	# no dongle
#from HamsterAPI.comm_usb import RobotComm	# yes dongle

################################
# Hamster control
################################
class RobotBehaviorThread(threading.Thread):
	def __init__(self):
		super(RobotBehaviorThread, self).__init__()
		self.go = False
		self.done = False
		return

	def run(self):
		robot=None
		while not self.done:
			if gRobotList:
				robot = gRobotList[0]	# max 1 robot per student
			if robot and self.go:
				#############################################
				# START OF YOUR WORKING AREA!!!
				#############################################
				# 
				# floor_l = robot.get_floor(0)
				# floor_r = robot.get_floor(1)
				# print "floor l/r", floor_l, floor_r
				#prox_l = robot.get_proximity(0)
				#prox_r = robot.get_proximity(1)
				robot.set_wheel(0,30)
				robot.set_wheel(1,30)
				time.sleep
				#############################################
				# END OF YOUR WORKING AREA!!!
				#############################################					
		# stop robot activities, such as motion, LEDs and sound
		# clean up after exit button pressed
		if robot:
			robot.reset()
			time.sleep(0.1)
		return

class GUI(object):
	def __init__(self, root, robot_control):
		self.root = root
		self.robot_control = robot_control
		root.geometry('250x30')
		root.title('Hamster Control')

		b1 = tk.Button(root, text='Go')
		b1.pack(side='left')
		b1.bind('<Button-1>', self.startProg)

		b2 = tk.Button(root, text='Exit')
		b2.pack(side='left')
		b2.bind('<Button-1>', self.stopProg)
		return
	
	def startProg(self, event=None):
		self.robot_control.go = True
		return

	def stopProg(self, event=None):
		self.robot_control.done = True		
		self.root.quit() 	# close window
		return

#################################
# Don't change any code below!! #
#################################

def main():
    # instantiate COMM object
    global gRobotList

    gMaxRobotNum = 1 # max number of robots to control
    comm = RobotComm(gMaxRobotNum)
    comm.start()
    print “Bluetooth starts”  
    gRobotList = comm.robotList

    behaviors = RobotBehaviorThread()
    behaviors.start()

    frame = tk.Tk()
    GUI(frame, behaviors)
    frame.mainloop()

    comm.stop()
    comm.join()
    print("terminated!")

if __name__ == "__main__":
    sys.exit(main())