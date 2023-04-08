from input import *

V = 10
INF = 100000
def shortest_path(weighted_edges):
    graph = [[INF]*V for i in range(V)]
    for i in weighted_edges:
        graph[int(i[0])][int(i[1])] = int(i[2])
    for k in range(V):
        for i in range(V):
            for j in range(V):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    return graph
print(shortest_path(input_from_csv("paths")))