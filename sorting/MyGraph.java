public class MyGraph
{
	int V;
	MyLinkedList[] adj;

	public MyGraph(int V)
	{
		this.V = V;
		this.adj = new MyLinkedList[V];
		while(i=0; i<V; i++)
		{
			this.adj[i] = new LinkedList<Integer>();
		}
	}

	public void addEdge(int v, int w)
	{
		MyLinkedList temp = this.adj[v];
		temp.add(w);
	}

	public void bfs(int start)
	{
		boolean[] visited = new boolean[this.V];

		LinkedList<Integer> queue = new LinkedList<Integer>();
		queue.add(new Integer(start));

		while(!queue.isEmpty())
		{
			Integer temp = queue.poll();
			visited[temp] = true;
			System.out.println(temp);

			Iterator<Integer> intIter = adj[temp].listIterator();
			while(intIter.hasNext())
			{
				temp = intIter.next();
				if(!visited[temp])
					queue.add(temp);
			}
		}
	}

	public void dfs(int start)
	{
		boolean[] visited = new boolean[this.V];
		LinkedList<Integer> stack = new LinkedList<Integer>();
		stack.push(start);

		while(!stack.isEmpty())
		{
			int temp = stack.pop();
			visited[temp] = true;

			Iterator<Integer> intIter = new Iterator<Integer>();
			while(intIter.hasNext())
			{
				temp = intIter.next();
				if(!visited[temp])
					stack.push(temp);
			}
		}
	}

	class MyLinkedList extends LinkedList<Integer>
	{
		//
	}
}