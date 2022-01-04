



class My_NodeData():

    def __init__(self,key:int,t=tuple ) ->None:
            if t == None:
                self.location = (0, 0, 0)
            else:
                self.location = (t[0], t[1], t[2])
            self.key = key
            self.prev = -1
            self.Weight=-1
            self.Tag = 0
            self.Info = " "

    def __str__(self):
        return " Node:"+self.key

    def getInfo(self) -> str:
        return self.Info

    def setInfo(self, x: str) -> None:
        self.Info = x

    def setTag(self,t:int)->None:
        self.Tag = t
    def getTag(self)->int:
        return self.Tag

    def getkey(self) -> int:
        #x=self.key
        return self.key

    def getlocation(self) -> tuple:
        x=tuple(self.location)
        return x

    def setlocation(self,tuple) -> None:
        self.location= tuple

    def getWeight(self) -> float:
        x=float(self.Weight)
        return x

    def setPrev(self, x: int) -> None:
        self.prev= x

    def getPrev(self) -> int:
        return self.prev

    def setWeight(self, x:float) -> None:
        self.Weight = x

    def __eq__(self, o: object) -> bool:
        if isinstance(o, My_NodeData):
            return self.key == o.key and self.Weight == o.Weight

    def __lt__(self, o):
        if isinstance(o, My_NodeData):
            return self.key == o.key and self.Weight == o.Weight


