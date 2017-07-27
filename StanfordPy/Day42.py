'''
/* =======================================================================
   (c) 2015, Kre8 Technology, Inc.
   Stater program of 3-state obstacle avoidance using FSM.

   Name:          starter1.py
   By:            Qin Chen
   Last Updated:  6/10/17

   PROPRIETARY and CONFIDENTIAL
   ========================================================================*/
'''
import sys
import time
import threading
import Tkinter as tk
import Queue
from HamsterAPI.comm_ble import RobotComm	

class Event(object):
    def __init__(self, event_type, event_data):
        self.type = event_type #string
        self.data = event_data #list of number or character depending on type

class StateMachine(object):
	def __init__(self, name, eventQ_handle):
		self.name = name	# machine name
		self.states = []	# list of lists, [[state name, event, transition, next_state],...]
		self.start_state = None
		self.end_states = []	# list of name strings
		self.q = eventQ_handle
		return

	def set_start_state(self, state_name):
		self.start_state = state_name
		return

	def get_start_state(self):
		return self.start_state
		
	def add_end_state(self, state_name):
		self.end_states.append(state_name)
		return
			
	def add_state(self, state, event, callback, next_state):
		self.states.append([state, event, callback, next_state]) # append to list
		return
	
	# you must set start state before calling run()
	def run(self):
		current_state = self.start_state
		#while not self.q.empty(): # for a machine that has end states
		while True:
			#print "current state", current_state
			if current_state in self.end_states:
				break
			#print "run", self.q.qsize()
			if not self.q.empty():
				e = self.q.get()
				for c in self.states:
					if c[0] == current_state and c[1] == e.type:
						#print('\nAction = %s, Transition = %s to %s' % (c[2], c[0], c[3]))
						#print('Transition = %s to %s' % (c[0], c[3]))
						c[2]()	# invoke callback function
						current_state = c[3] 	# next state
						break	# get out of inner for-loop
		return

################################
# Hamster control
################################
class RobotBehavior(object):
	def __init__(self):
		self.done = False	# set by GUI button
		self.go = False		# set by GUI button
		self.robot = None
		self.q = Queue.Queue()	# event queue for FSM
		self.spawn_threads()
		return

	def spawn_threads(self):
		###########################################################
		# 1. DONE create a watcher thread that reads sensors and registers events: obstacle on left, right or no obstacle. This
		# 	thread runs the method event_watcher() you are to implement below.
		# 2.DONE populate FSM(StateMachine) with avoidance states, set start state and create a thread to run the machine
		###########################################################	
		event_watcher = threading.Thread(name='event_watcher',target=self.event_watcher, args=(self.q,))

		event_watcher.daemon = True

		event_watcher.start()

		sm = StateMachine('Parking Ticket FSM', self.q)

		self.event_watcher = event_watcher

		#machine = threading.Thread(name='state machine',target=StateMachine.run, args=('Parking Ticket FSM', self.q))	

		sm.add_state('Forward', 'clear', self.go_forward, 'Forward')
		sm.add_state('Forward', 'robs', self.go_left, 'Right')
		sm.add_state('Forward', 'lobs', self.go_right, 'Left')

		sm.add_state('Left', 'lobs', self.go_left, 'Left')
		sm.add_state('Left', 'robs', self.go_left, 'Left')
		sm.add_state('Left', 'clear', self.go_forward, 'Forward')

		sm.add_state('Right', 'lobs', self.go_right, 'Right')
		sm.add_state('Right', 'robs', self.go_right, 'Right')
		sm.add_state('Right', 'clear', self.go_forward, 'Forward')

		sm.set_start_state('Forward')

		t = threading.Thread(name='FSM', target=sm.run)
		t.daemon = True
		t.start()

		

	def event_watcher(self, q):
		just_turned_on = True

		print "starting the event watcher thread"

		while not self.done:
			if gRobotList and self.go:
				#print "in loop"
				self.robot = gRobotList[0]
				if just_turned_on:
					#time.sleep(1)
					just_turned_on = False #the first time the robot connect, sensor data is unavailable the first second or so
				###########################################################
				# DONEImplement event producer here. The events are obstacle on left, right or no obstacle. Design your
				# logic for what event gets created based on sensor readings.

				prox_l = self.robot.get_proximity(0)

				prox_r = self.robot.get_proximity(1)

				print prox_l, prox_r

				if (prox_l > 5 or prox_r > 5):
					#print "obstacle detected, q1: %d %d" % (prox_l, prox_r)
					if prox_l > prox_r:
                    
						lobs = Event("lobs", [prox_l, prox_r])
						q.put(lobs)
					elif prox_r > prox_l:

						robs = Event("robs", [prox_l, prox_r])
						q.put(robs)
				else:
					clear = Event("clear", [prox_l, prox_r])
					q.put(clear)
				#print "event watcher: ", q.qsize()

				###########################################################
				time.sleep(0.01)
			# else:
			# 	print "waiting for robot in watcher"
		return

	#######################################
	# DONE Implement Hamster movements to avoid obstacle
	#######################################
	def go_left(self):
		a = self.q.get()
		self.robot = gRobotList[0]
		self.robot.set_wheel(0, -(a.data[0]*3))
		self.robot.set_wheel(1, (a.data[1]*3))
	def go_right(self):
		a = self.q.get()
		self.robot = gRobotList[0]
		self.robot.set_wheel(0, (a.data[0]*3))
		self.robot.set_wheel(1, -(a.data[1]*3))

	def go_forward(self):
		self.robot = gRobotList[0]
		self.robot.set_wheel(0, 100)
		self.robot.set_wheel(1, 100)
		  
class GUI(object):
	def __init__(self, root, robot_control):
		self.root = root
		self.robot_control = robot_control
		root.geometry('300x350')
		root.title('Hamster Control')

		canvas = tk.Canvas(root, bg="white", width=300, height=250)
		canvas.pack(expand=1, fill='both')
		canvas.create_rectangle(175, 175, 125, 125, fill="green")

		b1 = tk.Button(root, text='Go')
		b1.pack()
		b1.bind('<Button-1>', self.startProg)

		b2 = tk.Button(root, text='Exit')
		b2.pack()
		b2.bind('<Button-1>', self.stopProg)
		return
	
	def startProg(self, event=None):
		self.robot_control.go = True
		return

	def stopProg(self, event=None):
		self.robot_control.done = True		
		self.root.quit() 	# close window
		return

def main():
    gMaxRobotNum = 1 # max number of robots to control
    comm = RobotComm(gMaxRobotNum)
    comm.start()
    print 'Bluetooth starts'
    global gRobotList
    gRobotList = comm.robotList

    behaviors = RobotBehavior()

    frame = tk.Tk()
    GUI(frame, behaviors)
    frame.mainloop()

    comm.stop()
    comm.join()
    return

if __name__ == "__main__":
    sys.exit(main())