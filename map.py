class Map:
    width = "0.0001"
    count = 0
    route = []

    def __init__(self,route):
        self.route = route
        
    def getNextPoint(self):
        if(self.count >= len(self.route)):
            return False
        tmp = self.count
        self.count += 1
        return self.route[tmp]
    
    def reset(self):
        self.count = 0

    def getNextPointN(self):
        tmp = self.getNextPoint()
        if(tmp == False):
            self.reset()
            tmp = self.getNextPoint()
        return tmp
    
class DongCao(Map):
    def __init__(self):
        super(DongCao,self).__init__([[114.36515,34.811720],[114.36516,34.81042],[114.36605,34.81042],[114.36605,34.811720]]) 
    