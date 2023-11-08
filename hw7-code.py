def get_initial_parents(graph:dict, initial:str) -> dict:
    parents = {}
    for node in graph.keys():
        if node != None and node != initial:
            parents[node] = None
    initial_neighbors = graph[initial]
    if initial_neighbors == None:   # Error Checking
        return None
    for key in initial_neighbors.keys():
        parents[key] = initial
    return parents
    
def get_initial_costs(graph:dict, initial:str) -> dict:
    costs = {}
    for node in graph.keys():
        if node != None: # and node != initial:
            costs[node] = float("inf")
    initial_neighbors = graph[initial]
    if initial_neighbors == None:   # Error Checking
        return None
    for key, value in initial_neighbors.items():
        costs[key] = value
    return costs

def find_lowest_cost_node(costs:dict, processed:list) -> str:
    lowest_cost = float("inf")
    lowest_cost_node = None
    # Go through each node.
    for node in costs:
        cost = costs[node]
        # If it's the lowest cost so far and hasn't been processed yet...
        if cost < lowest_cost and node not in processed:
            # ... set it as the new lowest-cost node.
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

def run_dijkstra(graph:dict, start:str, finish:str) -> list:
    processed = [] 
    parents = get_initial_parents(graph, start)
    costs = get_initial_costs(graph, start)
    node = find_lowest_cost_node(costs,processed)


    # print("costs:", costs)
    # print("lowest cost node:", node)

    while node is not None:     
        cost = costs[node]
        # print("cost:", cost)
        neighbors = graph[node] 
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost 
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs,processed)

    path = [finish] 
    node = finish
    while (node != start):
        if parents[node] != None:
            node = parents[node]
            path = [node] + path

    
    return path


#Main:
# graph = {'start': {'a': 6, 'b': 2}, 'a': {'fin': 1}, 'b': {'a': 3, 'fin': 5}, 'fin': {}}
# path = run_dijkstra(graph, 'start', 'fin')
# print("The shortest path is", path)
graph2 = {'Book': {'LP': 5, 'Poster': 0}, 'LP': {'Bass': 15, 'Drum':20}, 'Poster': {'Bass':20, 'Drum':35}, 
          'Drum': {'Piano':10}, 'Bass': {'Piano':20}, 'Piano': {}}
path2 = run_dijkstra(graph2, 'Book', 'Piano')
print("The shortest path is", path2)

campus = {}
campus["King"] = {"Cutter":2, "Campus Center":3, "Chapin":2, "Paradise Pond":3}
campus["Lamont"] = {"Cutter":2, "Gillett":3}
campus["Neilson"] = {"Campus Center":3, "Gillett":3, "Seelye":4, "Ford":4, "Alumnae Gym":3, "Burton":3, "Chapin":4}
campus["Josten"] = {"Sage":1, "Ford":1}
campus["Ford"] = {"Gym":1, "Josten":1, "Sage":1, "Tyler":3, "Alumnae Gym":3, "Neilson":4, "Seelye":2}
campus["Campus Center"] ={"King":3, "Cutter":3, "Gillett":3, "Neilson":3, "Seelye":4, "Chapin":2}
campus["Sage"] = {"Josten":1, "Ford":1, "Tyler":2, "Gym": 2}
campus["Seelye"] = {"Campus Center":4, "Neilson":4, "Ford":2, "Gillett":4}
campus["Alumnae Gym"] = {"Ford":3, "Neilson":3, "Burton":4, "Tyler":3}
campus["Gym"] = {"Sage":2, "Ford":1}
campus["Stoddard"] = {"Gillett":2}
campus["Paradise Pond"] = {"King":3, "Tyler":2, "Burton":3}
campus["Gillett"] = {"Lamont":3, "Neilson":3, "Seelye":4, "Stoddard":2, "Campus Center":3}
campus["Chapin"] = {"King":2, "Neilson":4, "Campus Center":2}
campus["Tyler"] = {"Sage":2, "Ford":3, "Alumnae Gym":3, "Paradise Pond":2}
campus["Cutter"] = {"King":2, "Campus Center":3, "Lamont":2}
campus["Burton"] = {"Alumnae Gym":4, "Paradise Pond":3, "Neilson":3}


def main():
    
    # print(campus)
    # Test Djikstra's Algorithm on Campus MAp from Cutter to Ford
    # print("Testing Djikstra's Algorithm on Campus Map from Cutter to Ford")
    # path = run_dijkstra(campus, "Cutter", "Ford")
    # print("The shortest path is", path)

    ### MAKE INTERACTIVE USER INTERFACE ###
    ## User can choose start and end locations
    print("Welcome to the Smith College Campus Map!")
    print(" Today, we're going to help you find the path from point A to B with the least foot traffic.")
    print("Here is a list of all the locations on campus:")
    for key in campus.keys():
        print(key)
    print("Please enter your starting location:")
    start = input()
    while start not in campus.keys():
        print("Sorry, that's not a valid location. Please try again:")
        start = input()
    print("Please enter your destination:")
    end = input()
    while end not in campus.keys():
        print("Sorry, that's not a valid location. Please try again:")
        end = input()
    path = run_dijkstra(campus, start, end)
    print("The path of least resistance is", path)


main()


