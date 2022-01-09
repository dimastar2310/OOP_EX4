# Ex4 OOP Pokemons Gotta catch them all,fast!
welcome to the 4rd assignment of our OOP course .
at this task we going to summarize all our projectst 
to 1. In the lest projects ,project 0 we talked about 
online implementation of elevators wich goal was to minimizing 
waiting time of passanger wich is famous OOP project we had server
that made us calls for seconds we didnt know furder data,in second 
project we did know the data we needed to improve first implementaion and make it offline,
3rd  project was implementing directed weighed graph with the algorithm
of dijakstra,Center of graph,IsConnected,Tsp in java after that 
we needed to implement it to python and now we have 4rd assignment 
witch is catching pokemons ,the task is: we have agents and pokemons 
the pokemons has value and there are constrains its online code witch means
we have client that hes Server ,he sends us pokemons in duration times,
and we dont have the data before we need to get best scores and do it fast,
becouse there is time limit too if eatting alot of pokemons the server generating
us more pokemons. 
The graph is continues in keys from 0 to n ,there might be biderational Edges for example
from Verstesis 5 to 6 and from 6 to 5 so we need to take it in mind .
pokemons wich are in right diraction from 5 to 6 we colored in blue and if the pokemon 
is sitting on Edge from 6 to 5 in other direction(in constrains that this part of the graph 
is bideratctional we mark them in red ,you can see it gui the task is too catch as much as possible
and making minimum move() functions wich are annoynsing the server tath we made change in our graph
for example if we sending the agent if we do it right we might going to need less moves
the graph has weights so if the lesser the weight the faster he passes from edge to edge
and there might be possibiliting that we dont update the server in time and he might not 
eat the pokemon ,the edge speed time pass calculated with formula edge.weight*1 .
we getting the data for each dt as json file ,the server/client has its own functions
,the server has data wich is in format of json we need to convert the data for java language
and work with it in our main class wich is student class we getting the connection with the server
we converting the pokemond and the agent and the graph are json data,intro to our functions below .


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
  e.g.,  <java -jar Ex4_Server_v0.0.jar 0>  (where the “0” parameter is a case between [0-15]) ,after that starting
  the program in main by pressing green button the seed should be from 30 seconds to 120 seconds depends on case you 
  will guy appears on the screen the brown dots are agents blue if edge_dest<edge.src the pokemons that lays on that edge 
  is blue and o.w red.

 # tests <br />
 ### test_DiGraph and Test_AlgoGraph <br />
- we chack every function with exmples to see the correctness of the function.also we check if we can show the graph like in the picture. <br />
  ![Alt text](https://github.com/shaimoo/OOP/blob/main/picture/graph.png "test")  <br />
- we check the Tsp func by this Graph  <br />
![Alt text](https://github.com/shaimoo/OOP/blob/main/picture/tsp.jpeg "jijkstra") 
