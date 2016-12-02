def addEdge(vertList, x, y):
    if vertList.get(x) == None:
        vertList[x] = []
    if vertList.get(y) == None:
        vertList[y] = []
    vertList[x].append(y)
    vertList[y].append(x)

def read(File_Name):
    File = open(File_Name, 'r')

    global vertList
    nodes = set()
    vertex_List = {}
    file_content = []

    for line in File:
        if line[len(line) - 1 == '\n']:
            line = line[:len(line) - 1]
        vertex = line.split(' ')
        x = vertex[0]
        y = vertex[1]

        addEdge(vertex_List, x, y)
    """for vertex in file_content:
        x = vertex[0]
        y = vertex[1]

        addEdge(vertList, x, y)
    n = int(input("Number of nodes: "))
    m = int(input("Number of edges: "))
    for i in range(0, m):
        x = int(input())
        y = int(input())
        addEdge(vertList, x, y)"""

def printList():
    for i in range(1, n+1):
        print(*vertList[i], sep=' ')
        print('\n')

def DFS(x):
    viz[x] = True
    for i in vertList[x]:
        if viz[i] == False:
            DFS(i)

def DFS_comp(x):
    viz[x] = True
    comp.append(x)
    for i in vertList[x]:
        if viz[i] == False:
            DFS_comp(i)

def DFS_cycle(x, father):
    viz[x] = True
    for i in vertList[x]:
        if viz[i] == False:
            if DFS_cycle(i, x) == True:
                return True
        elif viz[i] == True & i != father:
            return True
    return False

def conex():
    global viz
    viz = [False for i in range(100)]
    DFS(1)
    nodes = 0
    for i in range(1, n+1):
        if viz[i] == True:
            nodes = nodes + 1
    if(nodes != n):
        print("The graph is conex.\n")
    else:
         print("The graph is not conex.\n")

def print_comp_conex():
    global viz, comp
    comp = []
    viz = [False for i in range(100)]
    nr = 0
    for i in range(1, n+1):
        if viz[i] == False:
            DFS_comp(i)
            print(*comp, sep = ' ')
            del comp[:]
            print('\n')

def check_cycle():
    global viz
    viz = [False for i in range(100)]
    if DFS_cycle(1, 0) == True:
        print("The graph has at least 1 cycle.\n")
    else:
        print("The graphs doesn't have any cycle.\n")

read('data.in')
check_cycle()