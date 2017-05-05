import GUI_Map as map
import GUI_DISTIONARY as dist

class Level:
    def __init__(self):
        self.levels = []
        for i in range(0,10,1):
            self.levels.append(map.Map(dist.FILEDIST[i]))
        pass
