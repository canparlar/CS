import Tkinter as tk
from HamsterAPI.comm_ble import RobotComm	

def main():
  
    global gRobotList

    gMaxRobotNum = 1 
    comm = RobotComm(gMaxRobotNum)
    comm.start()
    print 'Bluetooth starts'
    gRobotList = comm.robotList

    frame = tk.Tk()
    frame.mainloop()

    comm.stop()
    comm.join()
    print("terminated!")

if __name__ == "__main__":
    main()
