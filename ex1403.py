def floyd_warshall(graph):
    distances = {vertex: {v: float('inf') for v in graph} for vertex in graph}  # Inicializa todas as distâncias como infinito

    # Inicializa as distâncias conhecidas
    for vertex in graph:
        distances[vertex][vertex] = 0  # A distância de um vértice para si mesmo é 0
        for neighbor, weight in graph[vertex].items():
            distances[vertex][neighbor] = weight  # Define as distâncias conhecidas entre os vértices

    # Calcula as distâncias mínimas entre todos os pares
    for k in graph:
        for i in graph:
            for j in graph:
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])  # Atualiza a distância mínima

    return distances
