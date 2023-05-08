import math
graph = [
    [0, 3, math.inf, 7],
    [8, 0, 2, math.inf],
    [5, math.inf, 0, 1],
    [2, math.inf, math.inf, 0]
]
num_nodes = len(graph)

distance = [[graph[i][j] for j in range(num_nodes)] for i in range(num_nodes)]

for k in range(num_nodes):
    for i in range(num_nodes):
        for j in range(num_nodes):
            if distance[i][j] > distance[i][k] + distance[k][j]:
                distance[i][j] = distance[i][k] + distance[k][j]

print("All Pair Shortest Path Distance Matrix: ")
for row in distance:
    print(row)