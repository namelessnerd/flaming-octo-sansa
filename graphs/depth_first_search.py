#this code does dfs, cycles, and toplogical sort. for just dfs, refer to dfs_simple. 

def dfs_visit(current_vertex, graph, parent, finishing_order= None):
	# this method takes a finishing order parameter to enable topological sort. calling it with None
	# will not enable topological sort
	# get all vertices that can be reached from the current vertex
	for reachable_vertex in graph[current_vertex]:
		# check if we have visited this vertex already. if so, we can skip it. Keep in mind, this might denote a cycle
		if reachable_vertex not in parent:
			# add this vertex to visited by assigning it a parent
			parent[reachable_vertex]= current_vertex
			# start a depth first search from this vertex. DFS_visit alters the parent and returns the same. so when the 
			# DFS of this vertex returns, we need to make sure that our set of visited vertexs is updated to use this information.
			# to aid topological sort, if called with a finising order, we store the information
			(parent, finishing_order)= dfs_visit(reachable_vertex, graph, parent, finishing_order) if finishing_order else  dfs_visit(reachable_vertex, graph, parent, finishing_order)

		# the else block detects cycles. for just dfs, we do not need the else block
		else:
			#this is only for detecting cycles. we set the current parent to the current vertex. This is the 
			# current parent of the reachable vertex. Note that in this implementation, we do not change 
			# the list of parents. instead, we create a temp to store that the reachable vertex can be reached from 
			# the current vertex. Now we iterate through the parents of the current vertex. If the current reachable
			#vertex is an anscestor of the current vertex, we have a cycle.
			current_parent= current_vertex
			parents=[current_parent]
			# iterate through the anscestors; we break if the reachable vertex is an anscestor or if we have reached a vertex
			# with no anscestor
			while current_parent and current_parent!=reachable_vertex:
				if parent[current_parent]:
					parents.append(parent[current_parent])
				current_parent= parent[current_parent]
			# check if the reachable vertex is an anscestor
			if reachable_vertex in parents:
					print 'CYCLE {0} '.format(parents)
	# check if the current vertex is already finished. it implies that 
	# the current vertex is reachable earlier from another node. in that case, that is a higher order than the
	# current iteration. Hence we keep earlier version. In other words, current vertex has another dependency that 
	# precedes the current dependency. For toplogical sort, all dependencies must be fulfilled prior to reaching a vertex.
	if current_vertex not in finishing_order:
		finishing_order.append(current_vertex)
	return (parent, finishing_order)

def dfs(v,g):
	parent={}
	finishing_order=[]
	for u in g.keys():
		if u not in parent:
			# set the parent of the current node to None. 
			parent[u]=None
			# call dfs visit starting with the current node
			dfs_result=dfs_visit(u, g, parent,[])
			# update parent
			parent.update(dfs_result[0])
			#update finishing order
			finishing_order+=dfs_result[1]
	print parent
	print finishing_order

def main():
	graph={'a':['b','d',],'b':['e',],'e':['d',],'d':[],'c':['e','f',], 'f':[],}
	dfs('a',graph)

if __name__ == '__main__':
	main()