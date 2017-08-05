 def connected(self, point1, point2, cell_list):
    for cell in cell_list:
       intersection1 = False
       intersection2 = False
   
    cellXmin = min(cell[0],cell[2])
    cellXmax = max(cell[0],cell[2])
    cellYmin = min(cell[1],cell[3])
    cellYmax = max(cell[1],cell[3])

    if point1[0] <= cellXmax and point1[0] >= cellXmin and point1[1] <= cellYmax and point1[1] >= cellYmin:
        intersection1 = True
    if point2[0] <= cellXmax and point2[0] >= cellXmin and point2[1] <= cellYmax and point2[1] >= cellYmin:
        intersection2 = True
    if intersection1 and intersection2:
        result = True
    else
        result = False

    return result 
    