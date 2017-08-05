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
import Tkinter as tk
import bfs_engine
import tk_simple_graph_display
import graphgen

def main():
    grid = input("Enter Grid:")
    obs=[]
    a = input("Enter an obs or enter 0")
    while (a != 0):
        obs.append(a)
        a = input("Enter an obs or enter 0")
    
    # start_node = str(input("Start Node (x-x):"))
    # end_node = str(input("End Node (x-x):"))
    start_node = '1-1'
    end_node = '5-4'
    graph, nodes_location = graphgen.main(grid,obs)
    
    print 'graph:', graph

    frame = tk.Tk()
    frame.title('Simple Graph Display')
    frame.geometry("400x400")
    display = tk_simple_graph_display.SimpleGraphDisplay(frame, graph, nodes_location, start_node, end_node)

    bfs = bfs_engine.BFS(graph)
    p = bfs.bfs_shortest_path(start_node, end_node)
    display.highlight_path(p)
    frame.mainloop()
    return

if __name__ == main():
    sys.exit(main())
