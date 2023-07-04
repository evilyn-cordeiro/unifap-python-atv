import heapq

def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}  # Inicializa todas as distâncias como infinito
    distances[start] = 0  # A distância para o vértice inicial é 0
    queue = [(0, start)]  # Fila de prioridade para manter os vértices a serem explorados

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)  # Extrai o vértice com a menor distância atual

        # Ignora se já encontrou uma distância menor anteriormente
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight  # Calcula a distância até o vizinho atual
            if distance < distances[neighbor]:  # Se uma distância menor for encontrada
                distances[neighbor] = distance  # Atualiza a distância mínima
                heapq.heappush(queue, (distance, neighbor))  # Adiciona o vizinho à fila de prioridade

    return distances
