import sys
from collections import namedtuple

pair = namedtuple('Pair', 'destination weight')
debug = False


class Graph:
    """Класс графа, на котором будет происходить поиск пути"""

    def __init__(self):
        self.graph = {}  # словарь: вершина → список пар (ребро, вес)

    def add(self, parent: str, child: str, weight: float):
        """Добавление вершины и ребра в граф"""
        if parent not in self.graph:
            self.graph[parent] = []
        if child not in self.graph:
            self.graph[child] = []

        self.graph[parent].append(pair(child, weight))

        if debug:
            print(f"Добавим в граф вершину '{parent}' с ребром весом {weight} к вершине '{child}'")

    def get_to_go(self, vertex: str):
        """Возвращает список смежных вершин"""
        return self.graph[vertex]


def find_path(graph: Graph, start: str, finish: str):
    """Жадный алгоритм поиска кратчайшего пути"""
    closed = set()  # Вершины, которые больше не рассматриваем
    used_edges = set()  # Использованные ребра
    lastv = start  # Текущая вершина
    lastv_weight = 0
    path = [start]  # Построенный путь

    while lastv != finish:
        if debug:
            print("Текущий путь:", *path, f"; Последняя вершина: '{lastv}', вес: {lastv_weight}")

        to_go = set(graph.get_to_go(lastv)).difference(closed)

        if debug:
            print("Из неё можно попасть в:", *to_go)

        if to_go:
            current_vertex, current_vertex_weight = min(to_go, key=lambda vertex: (vertex[1], vertex[0]))

            if debug:
                print(f"Выбрана вершина '{current_vertex}' с минимальным весом {current_vertex_weight}")

            if (lastv, current_vertex) in used_edges:
                if debug:
                    print(f"Ребро {lastv} → {current_vertex} уже использовано")
                closed.add((current_vertex, current_vertex_weight))
            else:
                if debug:
                    print(f"Ребро {lastv} → {current_vertex} используется впервые. Добавляем в путь.")
                path.append(current_vertex)
                used_edges.add((lastv, current_vertex))
                lastv = current_vertex
                lastv_weight = current_vertex_weight
        else:
            if debug:
                print(f"Вершина '{lastv}' — лист. Возврат к предыдущей вершине '{path[-1]}'\n"
                      f"Добавляем её в закрытые.")
            closed.add((lastv, lastv_weight))
            path.pop()
            lastv = path[-1]

    if debug:
        print("Путь найден:")
    return path


if __name__ == "__main__":
    start, finish = input("Введите начальную и конечную вершины через пробел: ").split()
    graph = Graph()

    print("Введите ребра в формате: from to weight (пустая строка или EOF для завершения):")

    while True:
        try:
            line = input()
            if not line.strip():
                break
            parent, child, weight = line.strip().split()
        except (EOFError, ValueError):
            break
        graph.add(parent, child, float(weight))

    if debug:
        print('\nГраф:')
        for key in graph.graph:
            print(f"{key}:", end=' ')
            for elem in graph.graph[key]:
                print(f"{elem.destination}-{elem.weight}", end=' ')
            print()

    print(*find_path(graph, start, finish), sep='')
