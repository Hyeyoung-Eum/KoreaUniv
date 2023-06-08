from heapq import heappush
from heapq import heappop
def Dijkstra(graph, graph_v, start) :
    h = list()
    connect = list()
    for i in range(0, len(graph)) :
        connect.append(False)
    
    heappush(h, (0, start))

    while (len(h) > 0) :
        pop_info = heappop(h)
        pop_weight = pop_info[0]
        pop_node = pop_info[1]
        if connect[pop_node] == False :
            connect[pop_node] = True
            print(graph_v[start], '->', graph_v[pop_node], '최단 시간 :', pop_weight)
            for i in range(0, len(graph)) :
                if (graph[pop_node][i] != 0) and (connect[i] == False) :
                    heappush(h, (pop_weight + graph[pop_node][i], i))
G = [[0, 50, 0, 10, 0], [0, 0, 50, 40, 0], [0, 40, 0, 0, 20],
     [0, 30, 0, 0, 0],
     [0, 10, 0, 0, 0]]

V = ['집', '경찰서', '소방서', '학교', '병원']
Dijkstra(G, V, 0)