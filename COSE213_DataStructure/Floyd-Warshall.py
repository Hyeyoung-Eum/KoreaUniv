def FloydWarshall(graph, graph_v, start) :
  for i in range(0, len(graph)) :
    for j in range(0, len(graph)) :
        if (i != j) and (graph[i][j] == 0) : graph[i][j] = float('inf')

    for mid in range(0, len(graph)) :
        for start in range(0, len(graph)) :
            for end in range(0, len(graph)) :
                new_weight = graph[start][mid] + graph[mid][end]
                graph[start][end] = min(graph[start][end], new_weight)

    for i in range(0, len(graph)) :
        for j in range(0, len(graph)) :
            print(graph_v[i], '->', graph_v[j], '최단 거리 :', graph[i][j])
    G = [[0, 30, 0, 20, 0], [40, 0, 0, -30, 0],
        [0, 50, 0, 0, 30],
        [0, 0, 0, 0, 60],
        [0, -20, 0, 0, 0]]
    V = ['집', '경찰서', '소방서', '학교', '병원']
    FloydWarshall(G, V, 0)