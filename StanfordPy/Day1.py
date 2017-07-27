'''
/* =======================================================================
   (c) 2015, Kre8 Technology, Inc.
   This is a program that is provided to students in Robot AI class.
   Students use this it to build different Hamster behaviors.

   Name:          tk_behaviors_starter.py
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
	def __init__(self, robotList):
		super(RobotBehaviorThread, self).__init__()
		self.go = False
		self.done = False
		self.robotList = robotList
		return

	def run(self):
		robot=None
		while not self.done:
			if self.robotList:
				robot = self.robotList[0]	# max 1 robot per student
			if robot and self.go:
				############################################# GO
				# robot.set_wheel(0,255)
				# robot.set_wheel(1,255)
				############################################# SQUARE
				# robot.set_wheel(0, 255)
				# robot.set_wheel(1, 255)
				# time.sleep(1.0)
				# robot.set_wheel(0, 0)
				# time.sleep(0.5)
				############################################# FOLLOW
				# pleft = robot.get_proximity(1)
				# pright = robot.get_proximity(0)
				# if pright > 30 and pleft > 30:
				# 	robot.set_wheel(1, 255)
				# 	robot.set_wheel(0, 255)
				# elif pleft > 30:
				# 	robot.set_wheel(0, 255)
				# 	robot.set_wheel(1, 0)
				# elif pright > 30 :
				# 	robot.set_wheel(0, 0)
				# 	robot.set_wheel(1, 255)
				# else:
				# 	robot.set_wheel(1, 0)
				# 	robot.set_wheel(0, 0)
				############################################# SHY
				# pleft = robot.get_proximity(1)
				# pright = robot.get_proximity(0)
				# if pleft > 30 and pright < 30 :
				# 	robot.set_wheel(1, -255)
				# 	robot.set_wheel(0, 0)
				# elif pright > 30 and pleft < 30:
				# 	robot.set_wheel(0, -255)
				# 	robot.set_wheel(1, 0)
				# elif pright > 30 and pleft > 30:
				# 	robot.set_wheel(0, -255)
				# 	robot.set_wheel(1, -255)
				# else:
				# 	robot.set_wheel(1, 0)
				# 	robot.set_wheel(0, 0)
                ############################################# Dance
            	pleft = robot.get_proximity(1)
				pright = robot.get_proximity(0)
				if pleft > 30 and pright < 30 :
					robot.set_wheel(1, -255)
					robot.set_wheel(0, 0)
				elif pright > 30 and pleft < 30:
					robot.set_wheel(0, -255)
					robot.set_wheel(1, 0)
				elif pright > 30 and pleft > 30:
					robot.set_wheel(0, -255)
					robot.set_wheel(1, -255)
                elif pright > 30 and pleft > 30:
    				robot.set_wheel(1, 255)
    				robot.set_wheel(0, 255)
    			elif pleft > 30:
    				robot.set_wheel(0, 255)
    				robot.set_wheel(1, 0)
    			elif pright > 30 :
    			    robot.set_wheel(0, 0)
    			    robot.set_wheel(1, 255)
				else:
					robot.set_wheel(1, 0)
					robot.set_wheel(0, 0)
		if robot:
			robot.reset()
			time.sleep(0.1)
		return

	def dance(self):
		#############################################
		robot.set_wheel(0,255)
		robot.set_wheel(1,255)
		#############################################
		if robot:
			robot.reset()
			time.sleep(0.1)
	def pause(self):
		#############################################
		robot.set_wheel(0,255)
		robot.set_wheel(1,255)
		#############################################
		if robot:
			robot.reset()
			time.sleep(0.1)

class GUI(object):
	def __init__(self, root, robot_control):
		self.root = root
		self.robot_control = robot_control
		root.geometry('450x30')
		root.title('Hamster Control')

		b1 = tk.Button(root, text='Go')
		b1.pack(side='left')
		b1.bind('<Button-1>', self.startProg)

		# b2 = tk.Button(root, text='Square')
		# b2.pack(side='left')
		# b2.bind('<Button-1>', self.robot_control.square)

		# b3 = tk.Button(root, text='Follow')
		# b3.pack(side='left')
		# b3.bind('<Button-1>', self.robot_control.follow)

		# b4 = tk.Button(root, text='Shy')
		# b4.pack(side='left')
		# b4.bind('<Button-1>', self.robot_control.shy)

		# b5 = tk.Button(root, text='Dance')
		# b5.pack(side='left')
		# b5.bind('<Button-1>', self.robot_control.dance)

		# b6 = tk.Button(root, text='Pause')
		# b6.pack(side='left')
		# b6.bind('<Button-1>', self.robot_control.pause)

		b7 = tk.Button(root, text='Exit')
		b7.pack(side='left')
		b7.bind('<Button-1>', self.stopProg)
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
    gMaxRobotNum = 1; # max number of robots to control
    comm = RobotComm(gMaxRobotNum)
    comm.start()
    print 'Bluetooth starts'
    robotList = comm.robotList

    behaviors = RobotBehaviorThread(robotList)
    behaviors.start()

    frame = tk.Tk()
    GUI(frame, behaviors)
    frame.mainloop()

    comm.stop()
    comm.join()
    print("terminated!")

if __name__ == "__main__":
    sys.exit(main())
