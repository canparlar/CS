import threading
import time
import Queue
import sys

aaron = False

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
						#print "FOUND MATCHING: ", c[0], e.type
						break	# get out of inner for-loop
		return


class move(threading.Thread):
	def __init__(self, path,end, start_int,RobotList):
		super(move, self).__init__()
		self.RobotList = RobotList
		self.done = False
		self.q = Queue.Queue()	# event queue for FSM
		self.spawn_threads()
		self.path = path
		self.end = end
		self.start_int = start_int
		return

	def spawn_threads(self):
		event_watcher = threading.Thread(name='event_watcher',target=self.event_watcher, args=(self.q,))
		event_watcher.daemon = True
		event_watcher.start()

		sm = StateMachine('Parking Ticket FSM', self.q)

		self.event_watcher = event_watcher

		sm.add_state('GoN', 'follow', self.go_follow, 'GoN')
		sm.add_state('GoN', 'inter', self.aaronFunction, 'DecideN')
		sm.add_state('GoN', 'done', self.finish, 'Done')

		sm.add_state('GoE', 'follow', self.go_follow, 'GoE')
		sm.add_state('GoE', 'inter', self.aaronFunction, 'DecideE')
		sm.add_state('GoE', 'done', self.finish, 'Done')		

		sm.add_state('GoW', 'follow', self.go_follow, 'GoW')
		sm.add_state('GoW', 'inter', self.aaronFunction, 'DecideW')
		sm.add_state('GoW', 'done', self.finish, 'Done')

		sm.add_state('GoS', 'follow', self.go_follow, 'GoS')
		sm.add_state('GoS', 'inter', self.aaronFunction, 'DecideS')
		sm.add_state('GoS', 'done', self.finish, 'Done')

		sm.add_state('DecideN', 'west', self.go_left, 'GoW')
		sm.add_state('DecideN', 'east', self.go_right, 'GoE')
		sm.add_state('DecideN', 'north', self.go_forward, 'GoN')
		sm.add_state('DecideN', 'done', self.finish, 'Done')

		sm.add_state('DecideE', 'north', self.go_left, 'GoN')
		sm.add_state('DecideE', 'south', self.go_right, 'GoS')
		sm.add_state('DecideE', 'east', self.go_forward, 'GoE')
		sm.add_state('DecideE', 'done', self.finish, 'Done')

		sm.add_state('DecideW', 'south', self.go_left, 'GoS')
		sm.add_state('DecideW', 'north', self.go_right, 'GoN')
		sm.add_state('DecideW', 'west', self.go_forward, 'GoW')
		sm.add_state('DecideW', 'done', self.finish, 'Done')

		sm.add_state('DecideS', 'east', self.go_left, 'GoE')
		sm.add_state('DecideS', 'west', self.go_right, 'GoW')
		sm.add_state('DecideS', 'south', self.go_forward, 'GoS')
		sm.add_state('DecideS', 'done', self.finish, 'Done')

		sm.set_start_state('GoN')

		t = threading.Thread(name='FSM', target=sm.run)
		t.daemon = True
		t.start()

	def event_watcher(self, q):
		just_turned_on = True

		print "starting the event watcher thread"
		aaron = False

		while not self.done:
			if self.RobotList:
				self.robot = self.RobotList[0]
				if just_turned_on:
					just_turned_on = False 
					time.sleep(2)
					
					curr = self.start_int
					i = 1
				if aaron == False:
				
					# Lf = self.robot.get_floor(0)
					# Rf = self.robot.get_floor(1)


					if onIntersection(self.robot):

						inter = Event("inter", [])
						q.put(inter)
						#time.sleep(1.1)
						aaron = True
					else:	
						follow = Event("follow", [])
						q.put(follow)
				
				else:
					
					if i == len(self.path):
						done = Event("done", [])
						q.put(done)

					else:
						curr = self.path[-i][1]
						next = self.path[-(i+1)][1]
						if curr[0]+1 == next[0]:
							east = Event("east", [])
							q.put(east)

						if curr[0]-1 == next[0]:
							west = Event("west", [])
							q.put(west)

						if curr[1]+1 == next[1]:
							south = Event("south", [])
							q.put(south)

						if curr[1]-1 == next[1]:
							north = Event("north", [])
							q.put(north)
						i+=1
						aaron = False
				time.sleep(0.01)
		return

	def go_left(self):
		print "LEFT going LEFT"
		self.robot = self.RobotList[0]
		self.robot.set_wheel(0, 50)
		self.robot.set_wheel(1, 50)
		time.sleep(0.2)
		self.robot.set_wheel(0, -50)
		self.robot.set_wheel(1, 50)
		time.sleep(0.5)

	def go_right(self):
		print "RIGHT going RIGHT"
		self.robot = self.RobotList[0]
		self.robot.set_wheel(0, 50)
		self.robot.set_wheel(1, 50)
		time.sleep(0.2)
		self.robot.set_wheel(0, 50)
		self.robot.set_wheel(1, -50)
		time.sleep(0.5)

	def go_forward(self):
		print "FORWARD going FORWARD"
		self.robot = self.RobotList[0]
		self.robot.set_wheel(0, 50)
		self.robot.set_wheel(1, 50)
		time.sleep(0.2)
		

	def aaronFunction(self):
		self.robot = self.RobotList[0]
		self.robot.set_wheel(0, 0)
		self.robot.set_wheel(1, 0)
		self.robot.set_led(0,1)
		self.robot.set_led(1,1)
		self.robot.set_buzzer(100)
		time.sleep(0.1)
		self.robot.set_buzzer(0)

	def finish(self):
		self.robot = self.RobotList[0]
		self.robot.set_led(0,5)
		self.robot.set_led(1,5)
		self.robot.set_buzzer(300)
		time.sleep(0.3)
		self.robot.set_buzzer(0)
		time.sleep(0.3)
		self.robot.set_buzzer(200)
		time.sleep(0.3)
		self.robot.set_buzzer(0)
		time.sleep(0.3)
		self.robot.set_buzzer(100)
		time.sleep(0.3)
		self.robot.set_buzzer(0)

	def go_follow(self):
		self.robot = self.RobotList[0]
		Lf = self.robot.get_floor(0)
		Rf = self.robot.get_floor(1)
		self.robot.set_led(0,0)
		self.robot.set_led(1,0)
		y = 25
		if (Lf < Rf+y and Lf > Rf-y) or (Rf < Lf+y and Rf > Lf-y):
			self.robot.set_wheel(0, 50)
			self.robot.set_wheel(1, 50)
		elif Lf > Rf:
			self.robot.set_wheel(0, 10)
			self.robot.set_wheel(1, -10)
		else:
			self.robot.set_wheel(0, -10)
			self.robot.set_wheel(1, 10)
		
		return

lastTrue = -1
def onIntersection(robot):
	global lastTrue
	if robot.get_floor(0) < 40 and robot.get_floor(1) < 40 and time.time() > lastTrue+.3:
		lastTrue = time.time()
		print lastTrue
		return True
	return False


