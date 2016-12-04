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

"""
def roy_floyd():
    n = 0
    for i in nodes:
        n = max(n, int(i)+1)

    dp = [[0 for i in range(n+2)] for y in range(n+2)]

    for i in nodes:
        for j in vList[i]:
            dp[int(i)][int(j)] = 1


    for k in range(1, n):
        for i in range(1, n):
            for j in range(1, n):
                if i != j:
                    if dp[i][k] != 0:
                        if dp[k][j] != 0:
                            if dp[i][j] > dp[i][k] + dp[k][j]:
                                dp[i][j] = dp[i][k] + dp[k][j]
                            elif dp[i][j] == 0:
                                dp[i][j] = dp[i][k] + dp[k][j]
    for i in range(1, n):
        for j in range(1, n):
            print(dp[i][j], sep=' ', end='')
        print()
"""

def shortest_path(x, y):
    x = str(x)
    y = str(y)
    viz.clear()
    viz.add(x)
    queue = [x]
    father = {x: str(0)}

    while len(queue) != 0:
        node = queue[0]
        queue.pop(0)
        for i in vList[node]:
            if i not in viz:
                viz.add(i)
                father[i] = node
                queue.append(i)
    path = []
    if y not in viz:
        return path

    while y != str(0):
        path.append(y)
        y = father[str(y)]
    path.reverse()
    return path


def menu():
    print("\nMenu options:")
    print("Option 1: Print the adjacency list of the graph.")
    print("Option 2: Check if the graph is conex.")
    print("Option 3: Print the conex components.")
    print("Option 4: Check if the graph has at least 1 cycle.")
    print("Option 5: Get the shortest path from x to y.")
    print("Option 6: Quit.\n")

    option = int(input("Select your option: "))

    if option == 1:
        print_graph()
    elif option == 2:
        check_conex()
    elif option == 3:
        print_comp_conex()
    elif option == 4:
        check_cycle()
    elif option == 5:
        x = input("Read starting node: ")
        y = input("Read ending node: ")
        path = shortest_path(x, y)
        print('Shortest path from ' + x + " to " + y + " is: ", end='')
        print(*path, sep=' ', end='\n\n')
    elif option == 6:
        return
    else:
        print("You have introduced a wrong option.")
    menu()

menu()
