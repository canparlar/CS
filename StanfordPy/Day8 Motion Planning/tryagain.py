    def compute_free_cells(cell_list, c_obs_list):
        xvalues = [] 
        border = cell_list.get() 
        f_cell_list = [] 
        
        xvalues.append(border[0])
        xvalues.append(border[2])

        for cobs in c_obs_list:
            if cobs[0] not in xvalues: 
                xvalues.append(cobs[0])
            if cobs[2] not in xvalues:
                xvalues.append(cobs[2])

        xvalues.sort(reverse = True)

        x2 = xvalues.pop()
        while xvalues:
            x1 = x2
            x2 = xvalues.pop()
            
            region = [x1, border[1], x2, border[3]]

            interObs = []


            for obs in c_obs_list:
                obsXmin = min(obs[0],obs[2])
                obsXmax = max(obs[0],obs[2])
                obsYmin = min(obs[1],obs[3])
                obsYmax = max(obs[1],obs[3])

                regionXmin = min(region[0], region[2])
                regionXmax = max(region[0], region[2])
                regionYmin = min(region[1], region[3])
                regionYmax = max(region[1], region[3])

                if ((obsXmin >= regionXmax or obsXmax <= regionXmin)) :
                    u = 1
                else:
                    interObs.append(obs)
            print 'Region = ', region
            print 'Obs in it = ',interObs
            if interObs:
                dividedRegions = []
                yvalues = []
                yvalues.append(region[1])
                yvalues.append(region[3])
                for obs in interObs:
                    yvalues.append(obs[1])
                    yvalues.append(obs[3])
                yvalues.sort(reverse = True)
                y2 = yvalues.pop()
                while yvalues:
                    y1 = y2
                    y2 = yvalues.pop()
                    for obs in interObs:
                        obsXmin = min(obs[0],obs[2])
                        obsXmax = max(obs[0],obs[2])
                        obsYmin = min(obs[1],obs[3])
                        obsYmax = max(obs[1],obs[3])
                        if y1 != obsYmin:
                            newRegion = [regionXmin,y1,regionXmax,y2]
                            interObs = []
                            for obs in c_obs_list:
                                obsXmin = min(obs[0],obs[2])
                                obsXmax = max(obs[0],obs[2])
                                obsYmin = min(obs[1],obs[3])
                                obsYmax = max(obs[1],obs[3])

                                regionXmin = min(newRegion[0], newRegion[2])
                                regionXmax = max(newRegion[0], newRegion[2])
                                regionYmin = min(newRegion[1], newRegion[3])
                                regionYmax = max(newRegion[1], newRegion[3])
                                if ((obsXmin >= regionXmax or obsXmax <= regionXmin)and(obsYmin >= regionYmax or obsYmax <= regionYmin)) :
                                    f_cell_list.append(newRegion)
                                else:
                                    interObs.append(obs)

                                if interObs:
                                    dividedRegions = []
                                    yvalues = []
                                    yvalues.append(region[1])
                                    yvalues.append(region[3])
                                    for obs in interObs:
                                        yvalues.append(obs[1])
                                        yvalues.append(obs[3])
                                    yvalues.sort(reverse = True)
                                    y2 = yvalues.pop()
                                    while yvalues:
                                        y1 = y2
                                        y2 = yvalues.pop()
                                        for obs in interObs:
                                            obsXmin = min(obs[0],obs[2])
                                            obsXmax = max(obs[0],obs[2])
                                            obsYmin = min(obs[1],obs[3])
                                            obsYmax = max(obs[1],obs[3])
                                            if y1 != obsYmin:
                                                newRegion = [regionXmin,y1,regionXmax,y2]
                                                f_cell_list.append(newRegion)
                        if [regionXmin,obsYmin,regionXmax,obsYmax] in f_cell_list:
                            f_cell_list.remove([regionXmin,obsYmin,regionXmax,obsYmax])
            else:
                f_cell_list.append(region)
        f_cell_list = list(map(list,set(map(tuple,f_cell_list))))
        return f_cell_list





