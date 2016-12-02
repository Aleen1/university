def add_vertex(list, x, y):
    if list.get(x) is None:
        list[x] = []
    list[x].append(y)

    if list.get(y) is None:
        list[y] = []
    list[y].append(x)


def add_Node(set, x, y):
    if x not in set:
        set.add(x)

    if y not in set:
        set.add(y)


def read(file_Name):
    File = open(file_Name, 'r')

    nodes = set()
    vertex_list = {}

    for line in File:
        if line[len(line) - 1 == '\n']:
            line = line[:len(line) - 1]
        vertex = line.split(' ')
        x = vertex[0]
        y = vertex[1]

        add_Node(nodes, x, y)
        add_vertex(vertex_list, x, y)

    return sorted(nodes), vertex_list

nodes, vList = read('data.in')
viz = set()
comp = []

def print_graph():
    for node in nodes:
        print(str(node) + ": " + str(vList[node]))


def DFS_conex(node):
    viz.add(node)
    nr_nodes = 1
    for i in vList[node]:
        if i not in viz:
            nr_nodes = nr_nodes + DFS_conex(i)
    return nr_nodes

def check_conex():
    viz.clear()
    if DFS_conex(nodes[0]) == len(nodes):
        print("The graph is conex.\n")
    else:
        print("The graph is NOT conex.\n")

def DFS_comp_conex(node):
    viz.add(node)
    comp.append(node)
    for i in vList[node]:
        if i not in viz:
            DFS_comp_conex(i)

def print_comp_conex():
    viz.clear()
    nr = 0
    for i in nodes:
        if i not in viz:
            DFS_comp_conex(i)
            nr = nr + 1
            print("Comp. no. ", nr, ": ", *sorted(comp), sep=' ')
            del comp[:]
    print()


def DFS_cycle(node, father):
    viz.add(node)
    for i in vList[node]:
        if i not in viz:
            if DFS_cycle(i, node) == True:
                return True
        elif i != father:
            return True
    return False

def check_cycle():
    viz.clear()
    for i in nodes:
        if i not in viz:
            if DFS_cycle(i, 0) == True:
                print("The graph has at least 1 cycle.\n")
                return False
    print("The graph has no cycles.\n")

check_conex()
print_comp_conex()
check_cycle()

"""def printList():
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
check_cycle()"""
