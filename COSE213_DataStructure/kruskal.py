def Kruskal(edges, vertexes) :
    edge_count = 0
    total_weight = 0
    union = dict()
    for each_vertex in vertexes :
        union[each_vertex] = each_vertex

    edges.sort()

    for each_edge in edges :
        if (union[each_edge[1]] != union[each_edge[2]]) :
            total_weight = total_weight + each_edge[0]
            edge_count = edge_count + 1
            print(each_edge[1], '과', each_edge[2], '이 연결되었습니다.')
            print('누적 가중치 합은', total_weight, '입니다.')
            new_value = union[each_edge[1]]
            old_value = union[each_edge[2]]
            for each_vertex in vertexes :
                if (union[each_vertex] == old_value) :
                    union[each_vertex] = new_value

        if edge_count >= (len(vertexes) - 1) :
            break

# E = [(30, '보람동', '해밀동'), (28, '보람동', '아름동'), (17, '보람동', '고운동'), (22, '아름동', '고운동'), (42, '해밀동', '고운동'), (19, '고운동', '도담동'), (15, '아름동', '도담동')]
# V = ['보람동', '해밀동', '아름동', '고운동', '도담동'] Kruskal(E, V)