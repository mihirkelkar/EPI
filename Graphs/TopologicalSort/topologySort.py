from collections import defaultdict

class Graph(object):
    def __init__(self):
        self.graph_list = defaultdict(list)
        self.visited = None
        self.stack = list()
    def addVertices(self, vertex_list, num):
        for ii in vertex_list:
          self.graph_list[ii[0]].append(ii[1])
        self.visited = [False] * num

    def topologicalSortUtil(self, ii):
        #print ii
        try:
          adj = self.graph_list[ii]
          #print adj
        except:
          adj = list()
        self.visited[ii - 1] = True
        for jj in adj:
          if not self.visited[jj - 1]:
            self.topologicalSortUtil(jj)
        self.stack.append(ii)
        #print str(ii) + "added"

    def TopologicalSort(self):
        for ii in self.graph_list.keys():
          if not self.visited[ii - 1]:
            self.topologicalSortUtil(ii)
        print self.stack[::-1]

def main():
    GraphOne = Graph()
    GraphOne.addVertices([(1, 2),(1, 3),(1, 4),(3, 5),(2, 5),(4, 5)], 5)
    GraphOne.TopologicalSort()

if __name__ == "__main__":
    main()
