Topological sorting is only possible in a directed acyclic graph.
it basically is a linear ordering of vertices such that for every directed edge uv, vertex u comes before v in the ordering.

So for example, in a graph

4 0
5 0
2 3
3 1
5 2

The Topological ordering would be  5 4 2 3 1 0
or 4 5 2 3 1 0


the first thing we do is represent the graph this way

4 : 0 1
5 : 0 2
2: 3
3: 1

Then we consider the first vertex.
  (say 4) and mark it as visited
  if it has adjacencies, we consider those first. (say 0) and call the sort function on it.
       [here we mark 0 as visited. 0 has no adjacencies, so we push it onto a stack]
  Now we move onto 1 and push it on the stack too coz no adjacencies.
  We push 4 onto the stack too     
 Now we move on to 5.
   (mark 5 as visited)
    Look at 0, its visited, so move on to 2 and call sort on it.
       (mark 2 as visited). 3 is its adjacency. So moving on to 3 (mark as visited)
          moving on to 1 coz its an adjacency of 3, (already visited, so move back)
          then back at 3. push 3 onto stack.
    push 2 onto stack
push 5 onto stack.  
