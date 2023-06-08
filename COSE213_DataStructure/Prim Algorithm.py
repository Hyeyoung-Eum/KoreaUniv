from heapq import heappush
from heapq import heappop

def Prim(graph, graph_v, start): #graph_v는 동네 이름

    h=list() #list를 우선순위 queue로 사용할 수 있게 해줌
    connect=list() #연결 여부를 받아 줌
    for i in range(0, len(graph)):
        connect.append(False) # connect=[F, F, F, F, F] 모두 연결X
    
    heappush(h, (0, start)) #h에서 어떤 힙을 push할 것인가? ex) (30, 도담), 시작점은 0이니까 0으로 표기
    total_weight=0 #총비용
    vertex_count=0 #연결한 것들의 수 : 다 연결되면 끊어야되니까

    while vertex_count < len(graph): #개통역이 5개가 될 때까지 계속 반복하겠다
        pop_info = heappop(h) #최솟값 뽑음, 그리고 날아가지 않게 저장
        pop_weight = pop_info[0]
        pop_node=pop_info[1]

        if connect[pop_node] == False:
            connect[pop_node] = True
            total_weight = total_weight + pop_weight
            vertex_count = vertex_count + 1
            print('새로 연결된 곳 :', graph_v[pop_node]) #이거 뭔지 모르겠음
            print('누적 가중치 합 :', total_weight)

            ###꼬리표 갱신###
            for i in range(0, len(graph)):
                if graph[pop_node][i] != 0 and connect[i] ==False:
                    heappush(h, (graph[pop_node][i]))

Prim(G,V,0)