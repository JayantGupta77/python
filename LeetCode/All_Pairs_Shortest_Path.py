def floyd_warshall(n, edges):
    dist = [[float('inf')] * n for _ in range(n)]
    # Distance to self is 0
    for i in range(n):
        dist[i][i] = 0

    for u, v, w in edges:
        dist[u][v] = w

    # Floyd-Warshall core algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

# Example usage (with correction for the given edges and n=6 for node 5)
n = 6
edges = [
    (0, 1, 3), (1, 2, -2), (2, 3, 1), (0, 3, 10),
    (1, 4, -2), (2, 5, 1), (1, 3, -2), (2, 4, 1)
]
result = floyd_warshall(n, edges)
for row in result:
    print(row)
