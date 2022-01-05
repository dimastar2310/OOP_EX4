"""
@author AchiyaZigi
OOP - Ex4
Very simple GUI example for python client to communicates with the server and "play the game!"
"""
from types import SimpleNamespace


from pygame.font import Font
from queue import PriorityQueue
from client import Client
import json
from pygame import gfxdraw
import pygame
from pygame import *

# init pygame
from client_python.DiGraph import DiGraph
from client_python.GraphAlgo import GraphAlgo

WIDTH, HEIGHT = 1080, 720
WHITE = (255, 255, 255)
RED = (255,0,0)
BLACK=(0,0,0)
# default port
PORT = 6666
# server host (default localhost 127.0.0.1)
HOST = '127.0.0.1'
pygame.init()
conter=0
screen = display.set_mode((WIDTH, HEIGHT), depth=32, flags=RESIZABLE)
clock = pygame.time.Clock()
pygame.font.init()
button = pygame.Rect(10,10,100,20)
client = Client()
client.start_connection(HOST, PORT)
points=0
pokemons = client.get_pokemons()
pokemons_obj = json.loads(pokemons, object_hook=lambda d: SimpleNamespace(**d))

print(pokemons)

graph_json = client.get_graph()
g = DiGraph()
FONT = pygame.font.SysFont('Arial', 20, bold=True)
# load the json string into SimpleNamespace Object

graph = json.loads(
    graph_json, object_hook=lambda json_dict: SimpleNamespace(**json_dict))

for n in graph.Nodes:
    x, y, _ = n.pos.split(',')
    n.pos = SimpleNamespace(x=float(x), y=float(y))
    g.add_node(n.id,(x,y,0))

for e in graph.Edges:
        # find the edge nodes
        src = next(n for n in graph.Nodes if n.id == e.src)
        dest = next(n for n in graph.Nodes if n.id == e.dest)
        g.add_edge(src.id,dest.id,e.w)

 # get data proportions
min_x = min(list(graph.Nodes), key=lambda n: n.pos.x).pos.x
min_y = min(list(graph.Nodes), key=lambda n: n.pos.y).pos.y
max_x = max(list(graph.Nodes), key=lambda n: n.pos.x).pos.x
max_y = max(list(graph.Nodes), key=lambda n: n.pos.y).pos.y

class Pokemon:

    def __init__(self,value:float,shortDist:float,location:tuple, t:int):
        self.t = t #0 its goint up -1 going down?
        self.flag = 0
        self.value = value
        self.shortDist = shortDist
        self.location = location



    #closest shortDist
    def __lt__(self, o): #self.value == o.value and self.shortDist == o.dis
        if isinstance(o, Pokemon):
            return self.shortDist == o.shortDist
    def setFlag(self,flag:int)->None:
        self.flag= flag
    def setShort(self,shortDist:float)->None:
        self.shortDist = shortDist
    def setSight(self,t:int)->None:
        self.t = t


class Agent:
    def __init__(self,location:tuple,id:int ,value:float , src:int , dest:int ,speed:float):
        self.location=location
        self.id=id
        self.value=value
        self.src=src
        self.dest=dest
        self.speed=speed
        self.pokemons = PriorityQueue()

    def addPokemons(self, p=Pokemon):
        self.pokemons.put(p)


def scale(data, min_screen, max_screen, min_data, max_data):
    """
    get the scaled data with proportions min_data, max_data
    relative to min and max screen dimentions
    """
    return ((data - min_data) / (max_data-min_data)) * (max_screen - min_screen) + min_screen


# decorate scale with the correct values

def my_scale(data, x=False, y=False):
    if x:
        return scale(data, 50, screen.get_width() - 50, min_x, max_x)
    if y:
        return scale(data, 50, screen.get_height()-50, min_y, max_y)

for n in g.get_all_v().values():
    x=my_scale(float(n.getlocation()[0]), x=True)
    y=my_scale(float(n.getlocation()[1]), y=True)
    n.setlocation((x,y,0))

my_pokimons=[]
my_agents=[]
radius = 15

client.add_agent("{\"id\":0}")
client.add_agent("{\"id\":1}")
client.add_agent("{\"id\":2}")
client.add_agent("{\"id\":3}")

# this commnad starts the server - the game is running now
client.start()

"""
The code below should be improved significantly:
The GUI and the "algo" are mixed - refactoring using MVC design pattern is required.
"""

while client.is_running() == 'true':
    pokemons = json.loads(client.get_pokemons(),
                          object_hook=lambda d: SimpleNamespace(**d)).Pokemons
    pokemons = [p.Pokemon for p in pokemons]
    for p in pokemons:
        x, y, _ = p.pos.split(',')
        p.pos = SimpleNamespace(x=my_scale(
            float(x), x=True), y=my_scale(float(y), y=True))
        x=my_scale(float(x),x=True)
        y=my_scale(float(y),y=True)
        my=Pokemon(value=float(p.value),t=int(p.type),location=(x,y),shortDist=0.0)
        my_pokimons.append(my)
        
    agents = json.loads(client.get_agents(),
                        object_hook=lambda d: SimpleNamespace(**d)).Agents
    agents = [agent.Agent for agent in agents]
    for a in agents:
        x, y, _ = a.pos.split(',')
        a.pos = SimpleNamespace(x=my_scale(
            float(x), x=True), y=my_scale(float(y), y=True))
        x=my_scale(float(x),x=True)
        y=my_scale(float(y),y=True)
        my=Agent(location=(x,y),id=int(a.id),value=float(a.value),src=int(a.src),dest=int(a.dest),speed=float(a.speed))
        my_agents.append(my)

    # check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 1 is the left mouse button, 2 is middle, 3 is right.
            if event.button == 1:
                # `event.pos` is the mouse position.
                if button.collidepoint(event.pos):
                    # Increment the number.
                    client.stop()

    # refresh surface
    screen.fill(Color(0, 0, 0))

    # draw nodes
    for n in graph.Nodes:
        x = my_scale(n.pos.x, x=True)
        y = my_scale(n.pos.y, y=True)

        # its just to get a nice antialiased circle
        gfxdraw.filled_circle(screen, int(x), int(y),
                              radius, Color(64, 80, 174))
        gfxdraw.aacircle(screen, int(x), int(y),
                         radius, Color(255, 255, 255))

        # draw the node id
        id_srf = FONT.render(str(n.id), True, Color(255, 255, 255))
        rect = id_srf.get_rect(center=(x, y))
        screen.blit(id_srf, rect)

    # draw edges
    for e in graph.Edges:
        # find the edge nodes
        src = next(n for n in graph.Nodes if n.id == e.src)
        dest = next(n for n in graph.Nodes if n.id == e.dest)


        # scaled positions
        src_x = my_scale(src.pos.x, x=True)
        src_y = my_scale(src.pos.y, y=True)
        dest_x = my_scale(dest.pos.x, x=True)
        dest_y = my_scale(dest.pos.y, y=True)

        # draw the line
        pygame.draw.line(screen, Color(61, 72, 126),
                         (src_x, src_y), (dest_x, dest_y))
    my_graph=GraphAlgo(g)
    pygame.draw.rect(screen, WHITE, button)
    text_surf = FONT.render("STOP", True, BLACK)
    text_rect = text_surf.get_rect(center=(55,16))
    screen.blit(text_surf, text_rect)
    info = str(client.get_info())
    g = info.split(":")
    conter=g[4].split(',')[0]
    font = pygame.font.SysFont(None, 24)
    text_moves = font.render('moves:'+conter, True, WHITE)
    screen.blit(text_moves, (20, 40))
    text_time_to_end = font.render('time to end:' + str(((float(client.time_to_end())/1000)%60)), True, WHITE)
    screen.blit(text_time_to_end, (20, 60))

    info=g[5].split(',')[0]
    text_points = font.render('points:' + info, True, WHITE)
    screen.blit(text_points, (20, 80))
    for p in pokemons:
          point = font.render(str(p.value), True, WHITE)
          screen.blit(point, ( int(p.pos.x),int(p.pos.y)+20 ))
    i=1
    for agent in agents:

        text_agent = font.render('agent :'+ str(agent.id)+' pos : x:'+str(agent.pos.x)+' y:'+str(agent.pos.y), True, WHITE)
        screen.blit(text_agent, (20, 80+20*i))
        i+=1
    # draw agents
    for agent in agents:
        pygame.draw.circle(screen, Color(122, 61, 23),
                           (int(agent.pos.x), int(agent.pos.y)), 10)
    # draw pokemons (note: should differ (GUI wise) between the up and the down pokemons (currently they are marked in the same way).
    for p in pokemons:
        if p.type == -1:
            pygame.draw.circle(screen, Color(0, 255, 255), (int(p.pos.x), int(p.pos.y)), 10)
        else:
            pygame.draw.circle(screen, RED, (int(p.pos.x), int(p.pos.y)), 10)
    # update screen changes
    display.update()

    # refresh rate
    clock.tick(60)

    # choose next edge
    for agent in agents:
        for p in pokemons:
            next_node=0
            if agent.dest == -1:
                next_node =my_graph.graph.get_edge(p.pos.x,p.pos.y)
                node_agent =my_graph.graph.get_agent(float(agent.pos.x),float(agent.pos.y))
                shortc=my_graph.shortest_path(node_agent,next_node[0])

            client.choose_next_edge(
                 '{"agent_id":'+str(agent.id)+', "next_node_id":'+str(next_node)[0]+'}')
            ttl = client.time_to_end()
            print(ttl, client.get_info())
            client.move()

# game over:
