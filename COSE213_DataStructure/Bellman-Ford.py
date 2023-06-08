def BellmanFord(graph, graph_v, start) :
    min_weight = list()
    for i in range(0, len(graph)) :
        min_weight.append(float('inf'))

    min_weight[start] = 0
    on_node = [start]
    new_on_node = list()

    for round in range(1, len(graph)) :
        for each_on_node in on_node :
            for i in range(0, len(graph)) :
                if (graph[each_on_node][i] != 0) :
                    new_weight = min_weight[each_on_node] + graph[each_on_node][i]
                    min_weight[i] = min(min_weight[i], new_weight)
                    new_on_node.append(i)
        on_node = new_on_node
        new_on_node = list()
    
    for i in range(0, len(graph)) :
        print(graph_v[start], '->', graph_v[i], '최단 시간 :', min_weight[i])

G = [[0, 30, 0, 20, 0], [40, 0, 0, -30, 0],
     [0, 50, 0, 0, 30],
     [0, 0, 0, 0, 60],
     [0, -20, 0, 0, 0]]
V = ['집', '경찰서', '소방서', '학교', '병원']
BellmanFord(G, V, 0)