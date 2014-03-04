
def dfs_visit(current_vertex, graph, parent):
	# get all vertices that can be reached from the current vertex
	print 'Current vertex {0}'.format(current_vertex)
	for reachable_vertex in graph[current_vertex]:
		# check if we have visited this vertex already. if so, we can skip it. Keep in mind, this might denote a cycle
		if reachable_vertex not in parent:
			# add this vertex to visited by assigning it a parent
			parent[reachable_vertex]= current_vertex
			# start a depth first search from this vertex. DFS_visit alters the parent and returns the same. so when the 
			# DFS of this vertex returns, we need to make sure that our set of visited vertexs is updated to use this information.
			parent= dfs_visit(reachable_vertex, graph, parent)
	print 'Finishing {0} with parent {1}'.format(current_vertex, parent)
	return parent

def dfs(v,g):
	parent={}
	for u in g.keys():
		if u not in parent:
			parent[u]= None
			parent.update(dfs_visit(u, g, parent))
	print parent

def main():
	graph={'a':['b','d',],'b':['e',],'e':['d',],'d':[],'c':['e','f',], 'f':[],}
	dfs('a',graph)

if __name__ == '__main__':
	main()