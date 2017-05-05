import Algorithm_BFS as b
import Algorithm_DFS as d

import GUI_DISTIONARY as dist

import Utilities as util

def depth(data):
    dfs = d.DFS(data)
    sol, count = dfs.traversalStateTree()
    path = util.findStep(sol)
    return path, count
def breadth(data):
    bfs = b.BFS(data)
    sol, count = bfs.traversalStateTree()
    path = util.findStep(sol)
    return path, count


for i in range(0,10,1):
    data = []
    with open(dist.FILEDIST[i], 'rt') as f:
        for line in f:
            data.append(line.strip())

    #path, step = breadth(data)
    path, step = depth(data)
    print 'level:', i
    print 'step:',step
    print 'path:',''.join(path)
    print

