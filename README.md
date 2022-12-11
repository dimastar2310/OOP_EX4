Object-Oriented Programming & Design - Ex4 (very last)

Abstract
This document presents the final (last) assignment for the OOP course (CS.Ariel 2021),
In this assignment, you will be asked to “put into practice” the main tools covered along the course, in particular, you are expected to design a “Pokemon game” in which given a weighted graph,  a set of “Agents” should be located on it so they could “catch” as many “Pokemons” as possible. The pokemons are located on the graph’s (directed) edges, therefore, the agent needs to take (aka walk)  the proper edge to “grab” the pokemon (see below for more info). Your goal is to maximize the overall sum of weights of the “grabbed” pokemons (while not exceeding the maximum amount of server calls allowed in a second - 10 max)

The Pokemon game
Here is a list of directions regarding the “Pokemon game”:
1.	The game is being played on a “server” that is given to you, you should design and implement the client-side (only).
2.	The server is a simple .jar file that can be run on any java machine (JDK 11 or above) in a command line, e.g.,  <java -jar Ex4_Server_v0.0.jar 0>  (where the “0” parameter is a case between [0-15]).
3.	After the server is running a client can connect to it (play with it) - you have two platforms to choose from: java or python (there is NO need to implement in both).
The java example is a very simple cmd example while the python includes a basic GUI (neither have any algorithms).




![alt text](https://github.com/dimastar2310/OOP_EX4/blob/main/Picture1.png)    ![alt text](https://github.com/dimastar2310/OOP_EX4/blob/main/Picture2.png)

Figure1 (left) case 0, the game as played using the python (pygame) example, the “agent” is marked in brown, while the Pokemon is marked in a light blue.
About the GUI:
 Clearly, there is a long way “to go” to make the UI on the left somewhat resemble the one on the right - yet keep in mind, this assignment is mainly regarding properly designing and implementing a software package - the GUI is (always) secondary to the algorithms.
However, it is important to create a clear scalable gui with a resizable window.
Make sure overall points, moves counter, and time to end in seconds are presented, as well as a “stop” button to gracefully stop the game at any time point.
Pokemons lying on downward edges should be differ from ones on upward edges.
It is recommended (for algo debug) to draw the nodes and agents ids as well as the pokemons values.
4.	After the game ends (each game has a fixed time - commonly 30-120 seconds) the results are printed - by the server. 

![alt text](https://github.com/dimastar2310/OOP_EX4/blob/main/Picture3.png) 
Figure2: the server cmd - the results are printed as a json string below the “Game over” 
5.	In this assignment, we are mainly interested in maximizing the overall score - which is denoted as “grade” - the sum of all the pokemon weight as caught by all the “Agents”. E.g., in Figure 2, the grade is 79, with 1760 moves (30 seconds game).
6.	The objective of this assignment is to maximize the grade - but without exceeding the maximal 10 calls to move per second (on average, that said, the above result is not valid as the number of “moves” is strictly above 300 = 30*10).
7.	The client (both in java and python) has the following api (all json based):
a.	Init the server with a case [0-15] from a command line.
b.	Get the underlining weighted (directed) graph - you can assume it is strongly connected (getGraph).
c.	Get the list of Pokemons (getPokemons), e.g., {"Pokemons":[{"Pokemon":{"value":5.0,"type":-1,"pos":"35.197656770719604,32.10191878639921,0.0"}}]} where value is the weight (grade), type is positive if the edge_dest > edge_src (else negative), and pos is the 2D position of it (here you need to find the edge - by the position & type). 
d.	Get a list of all the Agents (in case an agent is on a node its “dest” is -1).
e.	Locate each Agent on a node (addAgent) - before the game starts.
f.	Start a game - each game has a fixed time - mostly 30-120 seconds.
g.	Get the remaining time (in mili seconds) for the game to be played
h.	Direct each agent to the next destination (chooseNextEdge) - this can be done only when the agent is on a node (not on an edge) - this is the main api for the algorithm.
i.	Move the agents: this is the main method that “plays the game” - in order 
for an Agent to grab a pokemon, the agent needs to be on the same (directed edge) & the server should be called (move) when the Agent is “close-enough” to the pokemon - Note: the exact distance is not given.
j.	Get the game info (getInfo): returns the grade, and the number of moves of the current game. This data is printed at the end of each game.


![alt text](https://github.com/dimastar2310/OOP_EX4/blob/main/Picture4.png) 


https://github.com/dimastar2310/OOP_EX4/blob/main/Picture4.png


Figure3: the main (java) api - the python is the same.


Working Tasks: 

Sage 1 - get it running + github the project.
Stage 2 - design the general algorithm (write it down properly in your github docs).
Stage 3 - implement the simplest version of a working code (this should include a debuggable GUI)
Stage 4 - Improve your code and start uploading your results to the Google form.
Stage 5 - Make sure you have all the needed documents including readme, algorithm definition, class diagram, “how to run”, results, tests (unitest / junit), and some images (and a short clip) as a wiki (github) project. Make sure there is a working release available for download, and a short clip 
Stage 6 - report your results here, make sure you report all the 16 cases [0-15].
Stage 7 - upload your github link here.


## classes 

### client <br />
  this class is server class and it has folowing functions
  | Name of function | Description |
  |------------------|-------------|
  | start_connection(self, ip, port)  | connection with server|
  | def __send_message(self, msg)  | try and catch error|
  | def get_agents(self)  | returns: json str of agents |
  | def add_agent(self, json_of_node)  | server function to add agents in json format|
  |def get_graph(self)|getting to user graph in json format|
  |def get_info(self)| returns info of current sicle in  game num of agents ,pokemons,moves |
  |def get_pokemons(self) | Returns the current dt seed of pokemons in json format|
  |def is_running(self) | return True if the game is still running False o.w.|
  |def time_to_end(self) |  return the time of the game|
  |def stop(self)|stopes the game and upload results |
  |def move(self)|activate all valid choose_next_edge calls|
  |choose_next_edge(self, next_agent_node_json)|choosing the next destination for a specific agent.|
  |log_in(self, id_str)|enter your id as str to login and upload your score to the web server|
  |stop_connection(self))|use it to close the connection 'gracefuly'.|
  
### student_code <br />
  this class is student class(main) first we making composition with
  client(server) setting pygame for gui,making connection with server
  seeting pygame variables ,getting the from the server and putting in our graph 
  that we made in 3rd task ,splitting the strings in json becouse its not fully json,
  adding the the nodes and edges wich are in json file they all represent graph putting them all
  in our graph,getting the agents,pokemons,data  in each dt in the while loop till the time ends.
  
  
  | Name of function | Description |
  |------------------|-------------|
  | def scale(data, min_screen, max_screen, min_data, max_data)  | rearenging scales for gui|
  | my_scale(data, x=False, y=False)  | the json files are too close in cordinates so we make am bigger|
  ### disctiption of student_code <br />
  loading data(current game) agents,pokemons ,appending screen for gui
  now the algorithm ,first we put the agent close to pokemon location that they eat them fast at first time , then     in down rows:we running on agents for each agent 
  we give him pokimon that he need to catch so they dont try to catch the same pokimon both of them ,if the agent 
  is on some vertesis agent.dest = -1 ,we starting to work with him
  becouse our functions works from vertesis to vertesis if its true 
  then the agent do shortpath Dijkstra's algorithm about the pokimon he need to catch. 
  we build en   Digraph class function that return the dest and src of pokrmon so if we go at the
  good way the agent eat the pokemon else he go the other way and eat him no never what
  so we do the shortpath between agent src and the pokimon src , if he didnt eat him he go to the dest and the to src.
     
  - the UML Diagram for algorithm is   <br />
![Alt text](https://github.com/dimastar2310/OOP_EX4/blob/main/Pokemons_catch.png) 
### My_Nodedata <br />
  this class implements NodeData interface represent node at graph
  that have id=name_of_node and location=(0,0,0) 
  
 
### DiGraph  <br />
  this class implements Graphinterface interface represent a weighted
  and directed graph.

  | Name of function | Description |
  |------------------|-------------|
  | init(self)       | constractor function|
  | get_v(self,key)  | returns the My_NodeData ig id equals key |
  | v_size(self)     | returns the size of the Nodes in the graph |
  | get_all_v(self)  | returns all the nodes in the graph by dict|
  | all_in_edges_of_node(self,id1: int)|return a dictionary of all the nodes connected to node_id|
  |all_out_edges_of_node(self, id1: int)| return a dictionary of all the nodes connected from node_id|
  |get_mc(self) | Returns the current version of this graph|
  |add_edge(self, id1: int, id2: int, weight: float) | Adds an edge to the graph ,return: True if the edge was added successfully, False o.w.|
  | add_node(self, node_id: int, pos: tuple = None) |   Adds a node to the graph.return: True if the node was added successfully, False o.w.|
  |remove_node(self, node_id: int)| Removes a node from the graph.return: True if the edge was removed successfully, False o.w.|
  |remove_edge(self, node_id1: int, node_id2: int)|Removes an edge from the graph.return: True if the edge was removed successfully, False o.w.|
  
### GraphAlgo  <br />
  this class implements GraphAlgointerface interface .<br />

 | Name of function | Description |
 |------------------|-------------|
 | get_graph(self)       | return the directed graph on which the algorithm works on. |
 |  DFS(self, id1: int)     | implementation of dfc algorithm do it about all the node. | 
 |  isConnected(self) | return if the graph is conect or no |
 | load_from_json(self, file_name: str)      | returns True if the loading was successful, False o.w. |
 |  save_to_json(self, file_name: str)      |  returns True if the loading was successful, False o.w. |
 |   shortest_path(self, id1: int, id2: int)       | using dijkstra algorithm . returns The distance of the path, a list of the nodes ids that the path goes through.   ![Alt text](https://github.com/shaimoo/OOP/blob/main/picture/dijkstra.jpeg "jijkstra") |
 | TSP(self, node_lst: List[int])     |  A list of the nodes id's in the path, and the overall distance |
 |  centerPoint(self)    | return The nodes id, min-maximum distance | 
 |  plot_graph(self)     |  If the nodes have a position, the nodes will be placed there.Otherwise, they will be placed in a random but elegant manner.return: None |
        

  ## how to download  <br />
- To download the task from GitHub, you should navigate to the top level of the project , and then a green "Code" download button will be visible on the right.
   Choose the Download ZIP option from the Code pull-down menu. That ZIP file will contain the entire repository content.
  ## how to use  <br />
- After you download the task at zip you need to extract  the zip file , then you need 
  to open cmd going to to your file location aka cd "file location" when you be on the file location
  you have to have java machine with (JDK 11 or above) in a command line write,
  e.g.,  <java -jar Ex4_Server_v0.0.jar 0> without <>  (where the “0” parameter is a case between [0-15]) ,after that starting
  the program in main by pressing green button the seed should be from 30 seconds to 120 seconds depends on case you 
  will guy appears on the screen the brown dots are agents blue if edge_dest<edge.src the pokemons that lays on that edge 
  is blue and o.w red.

 # tests <br />
 ### test_DiGraph and Test_AlgoGraph <br />
- we chack every function with exmples to see the correctness of the function.also we check if we can show the graph like in the picture. <br />
  ![Alt text](https://github.com/shaimoo/OOP/blob/main/picture/graph.png "test")  <br />
- we check the Tsp func by this Graph  <br />
![Alt text](https://github.com/shaimoo/OOP/blob/main/picture/tsp.jpeg "jijkstra") 
