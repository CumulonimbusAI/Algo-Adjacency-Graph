"""
A Python program to demonstrate the adjacency
list representation of the graph

Write a Python program to implement "Adjacency Graph".

  0 1 2 3 4
------------
0 0 0 1 0 0
1 0 1 1 1 0
2 1 1 1 1 1
3 0 1 1 1 0
4 0 0 1 0 0 

"""

# A class to represent the adjacency list of the node
class AdjNode:
        def __init__(self, data):
                self.vertex = data
                self.next = None


# A class to represent a graph. A graph
# is the list of the adjacency lists.
# Size of the array or hash table will be the no. of the
# vertices "V"
class Graph:
        def __init__(self, vertices):
                #initialize vertices in the graph
                self.V = vertices
                # create a list of vertices and initialize it.
                self.graph = self.V * [None]

        # Function to add an edge in an undirected graph
        def add_edge(self, src, dest):
                # Adding the node to the source node
                node = AdjNode(dest)
                node.next = self.graph[src]
                self.graph[src] = node

        # Function to print the graph
        def displayGraph(self):
                for i in range(self.V):
                        print("[",i,"]",":", end=" ");
                        temp = self.graph[i]
                        while temp:
                                print(" -> {}".format(temp.vertex), end="")
                                temp = temp.next
                        print(" \n")


# Driver program to the above graph class
if __name__ == "__main__":
        V = 5
        graph = Graph(V)

        graph.add_edge(0,2)
        graph.add_edge(1,1)
        graph.add_edge(1,2)
        graph.add_edge(1,3)
        graph.add_edge(2,0)
        graph.add_edge(2,1)
        graph.add_edge(2,2)
        graph.add_edge(2,3)
        graph.add_edge(2,4)
        graph.add_edge(3,1)
        graph.add_edge(3,2)
        graph.add_edge(3,3)
        graph.add_edge(4,2)
        
        graph.displayGraph()
    
