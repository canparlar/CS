

def main(grid,obs):
	graph ={}
	locs = []
	rows = grid[1]
	cols = grid[0]
	for i in range(1,rows+1):
		for j in range(1,cols+1):

			node_name = str(i) + '-' + str(j)

			for y in range(len(obs)):
				if obs[y][0] == i and obs[y][1] == j:
					break
			else:
				l = []
				if i-1 != 0:
					l.append(str(i-1)+'-'+str(j))

				if i != rows:
					l.append(str(i+1)+'-'+str(j))

				if j-1 != 0:
					l.append(str(i)+'-'+str(j-1))

				if j != cols:
					l.append(str(i)+'-'+str(j+1))

				for y in range(len(obs)):
					obs_name = str(obs[y][0]) + '-' + str(obs[y][1])
					if obs_name in l:
						l.remove(obs_name)
					
				graph[node_name] = set(l)

				a = (node_name, [i,j])
				locs.append(a)

	# graph = {'1-1': set(['1-2', '1-2']),
	# '2-1': set(['1-1', '3-1', '2-2']),
	# '3-1': set(['2-1', '3-2']),
	# '1-2': set(['1-1', '1-3','2-2']),
	# '2-2': set(['1-2','2-3', '2-1','3-2']),
	# '3-2': set(['2-2','3-1','3-3']),
	# '1-3': set(['2-3','1-2']),
	# '2-3': set(['3-3','1-3','2-2']),
	# '3-3': set(['2-3','3-2'])}

	return graph, locs