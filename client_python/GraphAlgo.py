import json

import math
import random
from collections import deque
from queue import PriorityQueue
from typing import List

from matplotlib import pyplot as plt

from client_python.DiGraph import DiGraph
from client_python.GraphAlgoInterface import GraphAlgoInterface
from client_python.GraphInterface import GraphInterface
from client_python.My_NodeData import My_NodeData


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, g=DiGraph):
        if g is None:
           self.graph=DiGraph()
        else:
            self.graph = g

    def get_graph(self) -> GraphInterface:
        return self.graph




    def DFS(self, id1: int) -> None:
        graph = self.graph


        stack = deque()
        stack.append(id1)

        n =  graph.get_v(id1)
        n.setTag(1) #mark as visited

        while len(stack) != 0:
            curr = stack.pop()
            #running on edges on keys <src,<dest,weight>>
            #neighbor = graph.all_in_edges_of_node(curr):
            for neighbor in graph.all_in_edges_of_node(curr):
                if graph.get_v(neighbor).getTag()!=1:
                       graph.get_v(neighbor).setTag(1)
                       stack.append(neighbor)



    def isConnected(self)->bool:
        g= self.graph


        if g == None:
            return True
        if g.e_size() == 0 or g.v_size() == 1:#maby () needed
            return True
        if g.v_size() > g.e_size() + 1:
            return False
        all_nodes = g.get_all_v().keys() #self might be needed
        for v in all_nodes:
              #g = My_NodeData(iterate_node.__next__())
              self.DFS(v)

              all_nodes2 = g.get_all_v().values()
              for v in all_nodes2:

                  if v.getTag() != 1 :
                      return False

                  v.setTag(0)



        return True

    def load_from_json(self, file_name: str) -> bool:

        graph=DiGraph()
        try:
            with open (file_name,"r") as f:
                my_list = json.load(f)
                for node in my_list["Nodes"]:
                    if 'pos' in my_list.keys():
                          pos = node["pos"]
                          s=pos.split(',')
                          x=float(s[0])
                          y=float(s[1])
                          z=float(s[2])
                          p=(x,y ,z)
                    else:
                        p=(0,0,0)
                    id = node["id"]
                    graph.add_node(node_id=id ,pos=p)
                for i in my_list["Edges"]:
                    Src = i["src"]
                    w=i["w"]
                    dest=i["dest"]
                    graph.add_edge(Src,dest,w)

            self.graph=graph
            return True

        except EOFError as e:
            print(e)
            return False

    def save_to_json(self, file_name: str) -> bool:
        try:
           with open(file_name , "w")as f:
               my_ans={}
               nodes=[]
               edeges=[]

               for node in self.graph.get_all_v().values():
                   nodes.append({"pos":node.getlocation(),"id": node.getkey()})

                   for edge , weith in self.graph.all_in_edges_of_node(node.getkey()).items():
                        edeges.append({"src":node.getkey() ,"wight":weith,"dest":edge})


               my_ans["Edges"]=edeges
               my_ans["Nodes"]=nodes

               json.dump(my_ans,indent=6 ,fp=f)


           return True

        except EOFError as e:
            print(e)
            return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        # returning path + distance
        g = self.graph
        first_res = 0
        pq = PriorityQueue()
        my_nodes = g.get_all_v().values()

        for node in my_nodes:
            node.setWeight(math.inf)
            node.setTag(-1)
            pq.put(node)

        start: My_NodeData = g.get_v(key=id1)
        start.setWeight(0)

        pq.put(start)
        while not pq.empty():

            n1: My_NodeData = pq.get()

            edges_of_n = g.all_in_edges_of_node(n1.getkey()).items()

            for dest, weight in edges_of_n:

                n2: My_NodeData = g.get_v(dest)
                right = n1.getWeight() + weight
                if right < n2.getWeight():
                    n2.setWeight(right)
                    n2.setTag(n1.getkey())
                    pq.put(n2)

        right: My_NodeData = g.get_v(id2)
        if right.getWeight() is math.inf:
            return math.inf, []
        path = []
        path.insert(0, right.getkey())
        pos = right.getTag()

        while pos != -1:
            path.insert(0, pos)
            pos = g.get_v(pos).getTag()
        return right.getWeight(), path


    def plot_graph(self) -> None:
        g=self.graph
        for i in g.get_all_v():
            location=g.get_v(i).getlocation()
            x=location[0]
            y=location[1]
            if (location[0] and location[1]) == 0:
                x=random.randrange(0,200)
                y=random.randrange(0,200)
                g.get_v(i).setlocation((x,y,0))
            plt.plot(float(x),float(y),marker='.' ,color="blue")
            plt.text(float(x),float(y),str(i),color="red",fontsize="20")
        for src in g.get_all_v():
            for dest in g.all_in_edges_of_node(src):
                l1=g.get_v(src).getlocation()
                l2=g.get_v(dest).getlocation()
                plt.annotate("", xy=(float(l1[0]),float(l1[1])), xytext=(l2[0],l2[1]), arrowprops=dict(arrowstyle="->"))
                plt.text( ((l1[0]+l2[0])/2) , ((l1[1]+l2[1])/2) , str(format(g.all_in_edges_of_node(src).get(dest) , ".2f")) , color="green" , fontsize="10" )
        plt.show()

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        g = self.graph
        x = GraphAlgo(g)

        ans = []
        dist = 0
        if len(node_lst) > 0:
            ans.append(node_lst[0])
            start = node_lst[0]
            node_lst_len = len(node_lst) + 2
            for i in range(1, node_lst_len):
                result = x.shortest_path(start, i)
                an = result[1]
                dist += result[0]
                start = i
                for j in an[1:]:
                    ans.append(j)

        return ans, dist

    def centerPoint(self) -> (int, float):
        max_center=1000000000.1
        center=1000000000.1
        node = -1
        node_center=-1
        g = self.graph
        y=GraphAlgo(g)
        if not self.isConnected():
                return (0,0)
        for node1 in g.get_all_v():
            max_len = 0
            for node2 in g.get_all_v():

                if node2 != node1 :
                    x=y.shortest_path(node1,node2)
                    x=x[0]
                    if max_len < x:
                        max_center=x
                        max_len=x
                        node_center=node1

            if center >max_center:
                  center=max_center
                  node=node_center
        return node,center