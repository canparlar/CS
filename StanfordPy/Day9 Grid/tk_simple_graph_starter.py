'''
/* =======================================================================
   (c) 2015, Kre8 Technology, Inc.

   Name:          tk_simple_graph_starter.py
   By:            Qin Chen
   Last Updated:  6/10/17

   PROPRIETARY and CONFIDENTIAL
   ========================================================================*/
'''

import sys
import threading
import Tkinter as tk
import bfs_engine
import tk_simple_graph_display
import graphgen
import movements
from HamsterAPI.comm_ble import RobotComm

def main():
    grid = [4,4]
    obs=[]
    a = input("Enter an obs or enter 0")
    while (a != 0):
        obs.append(a)
        a = input("Enter an obs or enter 0")
    
    # start_node = str(input("Start Node (x-x):"))
    # end_node = str(input("End Node (x-x):"))
    start_node = '1-1'
    start_int = [1,1]
    end_node = '4-4'
    end_int = [4,4]
    graph, nodes_location = graphgen.main(grid,obs)
    
    print 'graph:', graph

    frame = tk.Tk()
    frame.title('Simple Graph Display')
    frame.geometry("400x400")
    display = tk_simple_graph_display.SimpleGraphDisplay(frame, graph, nodes_location, start_node, end_node)

    bfs = bfs_engine.BFS(graph)
    p = bfs.bfs_shortest_path(start_node, end_node)
    l = display.highlight_path(p)
    gMaxRobotNum = 1; # max number of robots to control
    comm = RobotComm(gMaxRobotNum)
    comm.start()
    print 'Bluetooth starts'
    robotList = comm.robotList
    movem = movements.move(l, start_int, end_int,robotList)
    movem.start()
    frame.mainloop()
  
    comm.stop()
    comm.join()
    print("terminated!")
if __name__ == main():
    sys.exit(main())
