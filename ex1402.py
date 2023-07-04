def bellman_ford(graph, start):
    distances = {vertex: float('inf') for vertex in graph}  # Inicializa todas as distâncias como infinito
    distances[start] = 0  # A distância para o vértice inicial é 0

    # Relaxa as arestas repetidamente
    for _ in range(len(graph) - 1):
        for vertex in graph:
            for neighbor, weight in graph[vertex].items():
                distance = distances[vertex] + weight  # Calcula a distância até o vizinho atual
                if distance < distances[neighbor]:  # Se uma distância menor for encontrada
                    distances[neighbor] = distance  # Atualiza a distância mínima

    # Verifica se há ciclos de peso negativo
    for vertex in graph:
        for neighbor, weight in graph[vertex].items():
            distance = distances[vertex] + weight
            if distance < distances[neighbor]:  # Se uma distância menor for encontrada
                raise ValueError("O grafo contém um ciclo de peso negativo")

    return distances
