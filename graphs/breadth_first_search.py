

def breadth_first_search(graph, starting_vertex):
	# store the number of steps in which we can reach a starting_vertex
	num_level= {starting_vertex:0,}
	#store the parent of each starting_vertex
	parent={starting_vertex:None,}
	#current level
	level= 1
	#store unexplored vertices
	unexplored=[starting_vertex]
	print type(graph)
	#while we have unexplored vertices, explore them
	while unexplored:
		#explore each unexplored vertices. We will keep a list of the next vertices to explore. This will be a list of 
		#all unexplored vertices that are reachable from the current unexplored vertices
		next_vertices_to_explore=[]
		for unexplored_vertex in unexplored:
			#get all the nodes we can reach from this starting_vertex
			for reachable_node in graph[unexplored_vertex]:
				#see if have visited this vertex. If we have, we will have a level value for initialization
				if reachable_node not in num_level:
					#we have reached a previously unreachable node in level steps
					num_level[reachable_node]= level
					# the parent of this node is the current unexplored vertex
					parent[reachable_node]= unexplored_vertex
					#add this to the next_vertices_to_explore
					next_vertices_to_explore.append(reachable_node)
		#now we have explored all unexplored vertices
		unexplored= next_vertices_to_explore
		print unexplored
		level+=1
	print parent
	print num_level

def main():
	graph={'a':['s','z',], 'z':['a',], 's':['a','x',], 'd':['x','c','f'], 'f':['d','c','v',], 'v':['f','c'], 'c':['d','f','x','v'], 'x':['s','d','c'],}
	breadth_first_search(graph,'s')

if __name__ == '__main__':
	main()