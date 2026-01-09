Graphs is a data structure used in Image Processing applications to detect segments, boundaries. Image processing and computer vision takes a wide range of applications. 

Consider an image whose pixel intensities are indicated as per matrix in the diagram.

<img width="1311" height="918" alt="image" src="https://github.com/user-attachments/assets/4057ed51-aad1-4246-a38e-906f480f61d2" />


The image shows a 4 row by 4 column matrix. The matrix can be represented in form of a graph by way of adjacency matrix. A graph is an Abstract Data Structure pair of (V,E) where V is the vertices [nodes] and E is the edges [links]. 

Consider the figure#1 in shown on the screen. It shows a graph mode with nodes A, B, C, D which is referred to as vertices and connected by links between A to B, D, B to C, C to D, D to B. These links are known as edges of the graph. The vertices are represented as V and edges are represented as E and therefore a graph is referred a G(V, E). The graph is known as directed graph as it has its edges with arrows pointing to destination from source. 

<img width="2347" height="1250" alt="image" src="https://github.com/user-attachments/assets/de68c78a-598d-488e-a7a5-07c6eca32d21" />


Moving on, we see figure#2 and figure#3 represent the way in which the graph can be traversed. Basically the graph can be traversed in adjacency matrix format as in figure 2 or by adjacency list format as in figure#3. In adjacency matrix format the vertices across the row indicate source and the ones across the columns indicate destination. We mark 1 if there is a path between source and destination otherwise 0. So as per the diagram in A row, we see 1's at B and D which means there is a directed path defined across them and 0's at A and C which tells there is no path defined between these vertices. Likewise we can verify with rows at B, C and D as well that make up the adjacency matrix. 

Now, figure#3 has a hash list with indices of the hash table representing the source vertex of the graph and nodes of the hash list reprenting the destination. So , if the hash index A has nodes B and D linked in its list it means that A has path towards B and D, likewise B has path towards C, C has path towards D and finally D has path towards B. This is generally known as ajdacency graph of directed graph. 

Lets now move towards understanding our python impementation to dump the adjacendy list for a directed graph. 

We begin with defining a list node that can be inserted to hash list as AdjNode at a given index in line#7. The AdjNode comprise of vertex which is the data of node represented as destination from the given source and a next pointer. 

Then a class to represent graph is defined. A graph is a list of the adjacency lists as we have discussed earlier.  The size of the hash table or array representing the adjacency list shall be equal to number of vertices 'V' @line#17.

A number of graph operations are defined in the graph class and those include adding edge to the graph, displaying the graph. Between line#25 and 29 , we have addEdge() with two parameters source and destination values alongwith the self graph object. Here list node is initialized with source as hash index and appended to the hash list. This forms a directed graph. If it was a undirected graph we would another node at hash index at destination with source value as node.

We then define displayGraph(). Here we traverse through the hash list which is the adjacency list on every index of hash table against every list until NULL is hit. For every index so called source of graph, the nodes at the list are printed which shall depict the traversal path. 

In the driver code, the vextex is set to 5 and graph object is initialized at line#45. Between line#47 and 59 graph edges are added. Then finally printed out by invoking displayGraph at line 61. 

