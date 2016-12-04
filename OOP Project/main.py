#fuction that adds a vertex to a dictionary(adjacency list)
def add_vertex(list, x, y):
    #allocate space for the list of node x
    #if this is the first time it's me
    if list.get(x) is None:
        list[x] = []
    #add node y to the list of nodes connected to x
    list[x].append(y)

    # allocate space for the list of node x
    # if this is the first time it's me
    if list.get(y) is None:
        list[y] = []
    # add node x to the list of nodes connected to y
    list[y].append(x)

#funtion that adds a node to a set
def add_Node(set, x, y):
    #if x is not already in set, then add it
    if x not in set:
        set.add(x)

    #if y is not already in set, then add it
    if y not in set:
        set.add(y)

#function that reads the input and return the set of nodes and the dictionary(adjacency list)
def read(file_Name):
    #open input file
    File = open(file_Name, 'r')

    #creating the set and dictionary that are going to be filled and returned
    nodes = set()
    vertex_list = {}

    #read each line in from the input file
    for line in File:
        #delete the '\n' from the end of the line
        if line[len(line) - 1 == '\n']:
            line = line[:len(line) - 1]

        #split the line in 2 parts
        vertex = line.split(' ')
        #x is first node of the vertex
        x = vertex[0]
        #y is the second node of the vertex
        y = vertex[1]

        #add x and y to the set of nodes
        add_Node(nodes, x, y)
        #add vertex x-y to the dictionary
        add_vertex(vertex_list, x, y)

    #return the set of nodes in sorted order and the dictionary(adjacency list)
    return sorted(nodes), vertex_list

#nodes - set of nodes
#vList - dictionary of vertexes
nodes, vList = read('data.in')
#set of visited nodes
viz = set()
#list of nodes in a connected component
comp = []

#function that prints the dictionary(adjacency list)
def print_graph():
    for node in nodes:
        print(str(node) + ": " + str(vList[node]))


#recursive function that traverses the graph from a starting node
#and return the number of nodes it has traversed
def DFS_conex(node):
    #add the current node in the visited set
    viz.add(node)
    #initial the number of nodes it traversed is 1(current node)
    nr_nodes = 1
    #for each neighbour of the current node
    for i in vList[node]:
        #if it has not been visited
        if i not in viz:
            #no of nodes will increase with the number of nodes the recursive function has traversed
            #from the neighbour of current node
            nr_nodes = nr_nodes + DFS_conex(i)
    #return the number of traversed nodes
    return nr_nodes

#fuction that checks if the graph is connected
def check_conex():
    #reseting the visited nodes set
    viz.clear()
    #if the recursive function(DFS_conex) has traversed all nodes
    #then the graph is connected otherwise it's not
    if DFS_conex(nodes[0]) == len(nodes):
        print("The graph is conex.\n")
    else:
        print("The graph is NOT conex.\n")

#recursive function that creates the connected component
#including the starting node
def DFS_comp_conex(node):
    #add the current node in the visited set
    viz.add(node)
    #add the current node in the connected component list
    comp.append(node)
    #for each neighbour of the current node
    for i in vList[node]:
        #if it has not been visited
        if i not in viz:
            #call the recursive function for it
            DFS_comp_conex(i)

#function that prints all the connected components
def print_comp_conex():
    #reseting the visited nodes set
    viz.clear()
    #number of connected components(initial equal to 0)
    nr = 0
    #for each node in the set of nodes
    for i in nodes:
        #if it doesn't belong to a connected component
        if i not in viz:
            #create one connected component including it
            DFS_comp_conex(i)
            #number of connected components is increased by 1
            nr = nr + 1
            #print the connected component
            print("Comp. no. ", nr, ": ", *sorted(comp), sep=' ')
            del comp[:]

#recursive function the returns whether the graph has a cycle or not
def DFS_cycle(node, father):
    # add the current node in the visited set
    viz.add(node)
    #for each neighbour of the current node
    for i in vList[node]:
        #if it has not been visited
        if i not in viz:
            #if the recursive function called for this neighbour says
            #it found a cycle than return True(we found a cycle)
            if DFS_cycle(i, node) == True:
                return True
        #if the neighbour is visited but it's not the father node of the current one
        #it means we hava cycle and we need to return True(we found a cycle)
        elif i != father:
            return True
    #if we get on this line it means we haven't found any cycle and we return false
    return False

#function that checks if the graph has a cycle or not
def check_cycle():
    #reseting the visited nodes set
    viz.clear()
    #for each node in the set of nodes
    for i in nodes:
        #if it has not been visited
        if i not in viz:
            #check whether the connected component including the current node has a cycle
            #If it does, then we print that and we close the function returning something
            if DFS_cycle(i, 0) == True:
                print("The graph has at least 1 cycle.\n")
                return True
    #If we get to this point it means we have not found any cycle so we print that
    print("The graph has no cycles.\n")

#function that return a set of nodes(shortest path) from node x to node y
def shortest_path(x, y):
    #x is the starting node
    x = str(x)
    #y is the ending node
    y = str(y)
    #reset the visited nodes set
    viz.clear()
    #add starting node to the visited set
    viz.add(x)
    #add x to queue
    queue = [x]
    #father of x is 0
    father = {x: str(0)}

    #while we have nodes in queue
    while len(queue) != 0:
        #we take the first node
        node = queue[0]
        #we pop it
        queue.pop(0)
        #for each neighbour of the current node
        for i in vList[node]:
            #if tha neighbour has not been visited
            if i not in viz:
                #add it to the visited nodes set
                viz.add(i)
                #father of the neighbour is the current node
                father[i] = node
                #add neighbour in the queue
                queue.append(i)

    #initially the path is empty
    path = []
    #if we didn't reach node y we return an empty path
    if y not in viz:
        return path

    #if we get here it means we found a path(the shortest one) from x to y
    #we reconstruct the path starting from y and going into it's father
    #untill we don't reach 0(father of x) we keep doing the same thing
    while y != str(0):
        #add y to the path
        path.append(y)
        #y becomes it's father
        y = father[str(y)]
    #we have to reverse the path because we constructed in reversed order
    path.reverse()
    #return the path
    return path

#menu function that prints all the available options and calls the right functions
def menu():
    print("\nMenu options:")
    print("Option 1: Print the adjacency list of the graph.")
    print("Option 2: Check if the graph is conex.")
    print("Option 3: Print the conex components.")
    print("Option 4: Check if the graph has at least 1 cycle.")
    print("Option 5: Get the shortest path from x to y.")
    print("Option 6: Quit.\n")
    #read the option user wants to access
    option = int(input("Select your option: "))

    #if option is equal to 1 we call the function that prints the graph(adjacency list)
    if option == 1:
        print_graph()
    #if option is equal to 2 we call the function that prints whether the graphs is
    #connected or not
    elif option == 2:
        check_conex()
    # if option is equal to 3 we call the function that prints all the connected components
    elif option == 3:
        print_comp_conex()
    #if option is equal to 4 we call the function that prints whether the graph has
    #a cycle or not
    elif option == 4:
        check_cycle()
    #if option is equal to 5 we call the function that prints the shortest path from x to y
    elif option == 5:
        #we first must read the starting and the ending points
        x = input("Read starting node: ")
        y = input("Read ending node: ")
        #call the function that returns the path and store the path into a variable
        path = shortest_path(x, y)
        #print the path
        print('Shortest path from ' + x + " to " + y + " is: ", end='')
        print(*path, sep=' ', end='\n\n')
    #if option is equal to 6 we quit the app
    elif option == 6:
        return
    #if the user introduced a wrong option we print the message
    else:
        print("You have introduced a wrong option.")
    #recall of menu function for further use of the app
    menu()

#first call of the menu function
menu()
