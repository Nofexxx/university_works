demo = True

class Edge:
    def __init__(
        self,
        destinationVertexName,
        capacity,
        currentFlow=0,
        wasRead=False
    ):
        if demo:
            print(f'\n[СОЗДАНИЕ_ЭКЗЕМПЛЯРА_РЕБРА]')
            print(f'Создание экземпляра Ребра:')
            print(f'- Вершина назначения: {destinationVertexName}')
            print(f'- Пропускная способность: {capacity}')
            print(f'- Текущий поток: {currentFlow}')
            print(f'- Было ли прочитано из входного графа: {wasRead}')

        self.destinationVertexName = destinationVertexName
        self.capacity = capacity
        self.currentFlow = currentFlow
        self.wasRead = wasRead


def sortGraph(graph):
    if demo:
        print('\n[СОРТИРОВКА] Сортировка графа по вершинам')

    for key in graph:
        graph[key] = sorted(graph[key], key=lambda x: x.destinationVertexName)

    return dict(sorted(graph.items()))


def getEdge(graph, source, destination):
    if demo:
        print(f'\n[ПОИСК_РЕБРА_В_ГРАФЕ]')

    if source in graph:
        for edge in graph[source]:
            if edge.destinationVertexName == destination:
                if demo:
                    print(f'Ребро найдено: {source} -> {destination}')
                return edge
    if demo:
        print(f'Ребро {source} -> {destination} не найдено')
    return None


def pathFlow(path, graph):
    if demo:
        print(f'\n[ВЫЧИСЛЕНИЕ_ПОТОКА]')
    minCapacity = float('inf')

    for i in range(1, len(path)):
        edge = getEdge(graph, path[i - 1], path[i])
        if edge:
            minCapacity = min(minCapacity, edge.capacity)
    return minCapacity


def pathFinder(start, end, graph):
    if demo:
        print(f'\n[ПОИСК_ПУТИ]')

    processed = []
    transitions = {}
    stack = [start]

    while stack:
        cur = stack.pop()
        if cur == end:
            path = []
            while cur != start:
                path.append(cur)
                cur = transitions[cur]
            path.append(start)
            path.reverse()
            return path

        for edge in graph.get(cur, []):
            if edge.destinationVertexName not in processed and edge.capacity > 0:
                if edge.destinationVertexName not in transitions:
                    transitions[edge.destinationVertexName] = cur
                    stack.append(edge.destinationVertexName)
        processed.append(cur)
    return None


def findFlow(start, end, graph):
    if demo:
        print('[ЗАПУСК_АЛГОРИТМА_ФОРДА_ФАЛКЕРСОНА]')

    totalFlow = 0

    while True:
        path = pathFinder(start, end, graph)
        if not path:
            break

        flow = pathFlow(path, graph)
        totalFlow += flow

        for i in range(1, len(path)):
            edge = getEdge(graph, path[i - 1], path[i])
            if edge:
                edge.capacity -= flow
                edge.currentFlow += flow

            reverseEdge = getEdge(graph, path[i], path[i - 1])
            if reverseEdge:
                reverseEdge.capacity += flow
                reverseEdge.currentFlow -= flow
            else:
                if path[i] not in graph:
                    graph[path[i]] = []
                graph[path[i]].append(Edge(path[i - 1], flow, -flow, False))
                graph = sortGraph(graph)
    return totalFlow


def logGraph(graph):
    if demo:
        print(f'\n[ЛОГИРОВАНИЕ_ГРАФА]')
        for source in graph:
            for edge in graph[source]:
                if edge.wasRead:
                    flowOutput = max(edge.currentFlow, 0)
                    print(f'{source} {edge.destinationVertexName} {flowOutput}')


def main():
    if demo:
        print(f'[ВВОД_ДАННЫХ]')

    edges = int(input())
    start = input()
    end = input()
    graph = {}

    for _ in range(edges):
        source, destination, weight = input().split()
        weight = int(weight)
        if source not in graph:
            graph[source] = []
        graph[source].append(Edge(destination, weight, 0, True))

    graph = sortGraph(graph)
    totalFlow = findFlow(start, end, graph)

    if demo:
        print('[РЕЗУЛЬТАТ]')
        print(totalFlow)
        logGraph(graph)


if __name__ == "__main__":
    main()
